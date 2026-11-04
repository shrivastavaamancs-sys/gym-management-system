from django.test import TestCase
import datetime
from .models import Trainer, Offer, Member

class GymModelTest(TestCase):
    def setUp(self):
        # Correctly creating an Offer using 'code' and 'valid_till'
        self.offer = Offer.objects.create(
            code="FESTIVE10", 
            discount_percentage=10, 
            valid_till=datetime.date(2026, 12, 31),
            is_active=True
        )
        
        # Creating a sample Trainer
        self.trainer = Trainer.objects.create(
            name="Rahul Sharma",
            specialty="Weight Training",
            phone="9876543210"
        )
        
        # Creating a sample Member
        self.member = Member.objects.create(
            name="Amit Kumar",
            phone="9123456789",
            plan="Monthly",
            trainer=self.trainer,
            applied_offer=self.offer
        )

    def test_member_creation(self):
        self.assertEqual(self.member.name, "Amit Kumar")
        self.assertEqual(self.member.trainer.name, "Rahul Sharma")
        self.assertEqual(self.member.applied_offer.code, "FESTIVE10")
        self.assertTrue(self.member.is_active)

    def test_get_final_fee_with_discount(self):
        # Monthly plan is ₹1,000 with a 10% discount -> Expected: ₹900
        self.assertEqual(self.member.get_final_fee(), 900)