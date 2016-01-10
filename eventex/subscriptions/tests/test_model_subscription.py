from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscripitionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name='Ricardo Luiz Viana',
                cpf='12345678901',
                email='richardluizv@gmail.com',
                phone='31-984260143'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Ricardo Luiz Viana', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must be False."""
        self.assertEqual(False, self.obj.paid)

