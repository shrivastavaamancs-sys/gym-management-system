from django.test import TestCase
from .models import Member, Trainer, Offer, ContactMessage
from datetime import date, timedelta

class GymModelTest(TestCase):
    def setUp(self):
        self.trainer = Trainer.objects.create(
            name="Rahul Sharma", 
            specialty="Weightlifting", 
            phone="9876543210"
        )
        self.offer = Offer.objects.create(
            code="FESTIVE10", 
            discount_percentage=10, 
            valid_till=date.today() + timedelta(days=10),
            is_active=True
        )

    def test_member_creation_and_fee(self):
        member = Member.objects.create(
            name="Aman Shrivastava",
            phone="8448377736",
            email="aman@example.com",
            plan="Monthly",
            trainer=self.trainer,
            applied_offer=self.offer
        )
        self.assertEqual(member.name, "Aman Shrivastava")
        self.assertEqual(member.get_final_fee(), 900.00)

    def test_contact_message_creation(self):
        msg = ContactMessage.objects.create(
            name="Test User",
            email="test@example.com",
            phone="9123456789",
            message="Hello Elite Fitness!"
        )
        self.assertEqual(msg.name, "Test User")