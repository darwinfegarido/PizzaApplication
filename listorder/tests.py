from django.test import TestCase
from .models import Pizza, PizzaType, Transaction
from decimal import Decimal

class PizzaTypeTestCase(TestCase):
    def setUp(self):
        PizzaType.objects.create(name="TestCase1")


    def test_pizza_type(self):
        TestCase1 = PizzaType.objects.get(name="TestCase1")

        self.assertEqual(TestCase1.name, "TestCase1")


class PizzaTestCase(TestCase):
    def setUp(self):
        type = PizzaType.objects.create(name="TestCase1")
        Pizza.objects.create(pizza_type_id=type, name="TestCase1", price=23.30)


    def test_pizza(self):
        TestCase1 = Pizza.objects.get(name="TestCase1")

        self.assertEqual(TestCase1.name, "TestCase1")
        self.assertAlmostEqual(TestCase1.price, Decimal('23.3'))


class TransactionTestCase(TestCase):

    def setUp(self):
        type = PizzaType.objects.create(name="TestCase1")
        pizza = Pizza.objects.create(pizza_type_id=type, name="TestCase1", price=10)
        Transaction.objects.create(pizza_id=pizza, quantity=20)


    def test_transaction(self):
        TestCase1 = Transaction.objects.get(pk=1)

        self.assertEqual(TestCase1.pizza_id.name, "TestCase1")
        self.assertEqual(TestCase1.pizza_id.price, Decimal('10'))
        self.assertEqual(TestCase1.pizza_id.price * TestCase1.quantity, Decimal('200'))
