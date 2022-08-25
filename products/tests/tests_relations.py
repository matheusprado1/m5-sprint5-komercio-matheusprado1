from django.test import TestCase

from ..models import Product
from accounts.models import Account


class ProductRelationTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user = Account.objects.create(
            username='zeze',
            password='1234',
            first_name='zezim',
            last_name='ze',
            is_seller=True
        )

        cls.products = [
            Product.objects.create(
                description='Legalzin',
                price=1000.0,
                quantity=1,
                is_active=True,
                seller_id=cls.user.id
            )
            for _ in range(3)
        ]

    def test_user_may_contain_products_films(self):
        self.assertEquals(len(self.products), self.user.products.count())

    def test_product_cannot_belong_to_more_than_one_user(self):

        user_2 = Account.objects.create(
            username='zezao',
            password='1234',
            first_name='zezasso',
            last_name='zezezeze',
            is_seller=True
        )

        for product in self.products:
            product.seller_id = user_2.id
            product.save()

        for product in self.products:
            self.assertNotIn(product, self.user.products.all())
            self.assertIn(product, user_2.products.all())
