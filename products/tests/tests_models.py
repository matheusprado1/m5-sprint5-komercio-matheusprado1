from django.test import TestCase

from products.models import Product
from accounts.models import Account


class ProductModelTest(TestCase):
    databases = {'dbsqlite', 'default'}

    @classmethod
    def setUpTestData(cls):

        cls.username = "jorel"
        cls.password = "1234"
        cls.first_name = "Irmão"
        cls.last_name = "Jorel"
        cls.is_seller = True

        cls.user = Account.objects.create(
            username=cls.username,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=cls.is_seller,
        )

        cls.description = "Microondas de Brinquedo"
        cls.price = 1.99
        cls.quantity = 3
        cls.is_active = True
        cls.seller_id = cls.user.id

        cls.product = Product.objects.create(
            description=cls.description,
            price=cls.price,
            quantity=cls.quantity,
            is_active=cls.is_active,
            seller_id=cls.seller_id
        )

    def test_product_has_information_fields(self):
        self.assertEqual(self.product.description, self.description)
        self.assertEqual(self.product.price, self.price)
        self.assertEqual(self.product.quantity, self.quantity)
        self.assertTrue(self.product.seller_id, self.seller_id)
        self.assertTrue(self.product.is_active)
