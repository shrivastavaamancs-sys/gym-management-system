from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.specialty})"


class Offer(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.IntegerField(help_text="Discount percentage (e.g., 10 for 10%)")
    valid_till = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} ({self.discount_percentage}% OFF)"

class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    PLAN_CHOICES = [
        ('Monthly', 'Monthly (₹1,000)'),
        ('Quarterly', 'Quarterly (₹2,700)'),
        ('Yearly', 'Yearly (₹10,000)'),
    ]
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='Monthly')
    
    FEE_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]
    fee_status = models.CharField(max_length=10, choices=FEE_CHOICES, default='Pending')
    
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    applied_offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-id']  # Newest members pehle dikhenge

    def __str__(self):
        return self.name

    def get_final_fee(self):
        plan_prices = {
            'Monthly': 1000,
            'Quarterly': 2700,
            'Yearly': 10000
        }
        base_fee = plan_prices.get(self.plan, 1000)
        if self.applied_offer and self.applied_offer.is_active:
            discount_amount = (base_fee * self.applied_offer.discount_percentage) / 100
            return int(base_fee - discount_amount)
        return base_fee