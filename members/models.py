from django.db import models
from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator
)
from django.utils import timezone
from decimal import Decimal

# Phone Number Validation
phone_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message="Enter a valid 10-digit Indian mobile number."
)

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=10,
        validators=[phone_validator]
    )
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.specialty})"

class Offer(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.IntegerField(
        help_text="Discount percentage (e.g. 10 for 10%)",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    valid_till = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} ({self.discount_percentage}% OFF)"

    def is_valid(self):
        return self.is_active and self.valid_till >= timezone.localdate()

class Member(models.Model):
    PLAN_CHOICES = [
        ('Monthly', 'Monthly (₹1,000)'),
        ('Quarterly', 'Quarterly (₹2,700)'),
        ('Yearly', 'Yearly (₹10,000)'),
    ]

    FEE_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=10,
        validators=[phone_validator]
    )
    email = models.EmailField(blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES,
        default='Monthly'
    )
    fee_status = models.CharField(
        max_length=10,
        choices=FEE_CHOICES,
        default='Pending'
    )
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members'
    )
    applied_offer = models.ForeignKey(
        Offer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members'
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_final_fee(self):
        plan_prices = {
            'Monthly': Decimal('1000.00'),
            'Quarterly': Decimal('2700.00'),
            'Yearly': Decimal('10000.00')
        }
        base_fee = plan_prices.get(self.plan, Decimal('1000.00'))

        if self.applied_offer and self.applied_offer.is_valid():
            discount = (
                base_fee *
                Decimal(self.applied_offer.discount_percentage)
                / Decimal('100')
            )
            return base_fee - discount

        return base_fee

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=10,
        validators=[phone_validator]
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        ordering = ['-created_at']