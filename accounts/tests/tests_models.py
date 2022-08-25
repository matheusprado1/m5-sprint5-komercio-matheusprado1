from django.test import TestCase
from ..models import Account


class AccountModelTest(TestCase):
    databases = {'dbsqlite', 'default'}

    @classmethod
    def setUpTestData(cls):
        cls.username = 'jorel'
        cls.password = '1234'
        cls.first_name = 'Irmão'
        cls.last_name = 'Jorel'
        cls.is_seller = False

        cls.user = Account.objects.create(
            username=cls.username,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=cls.is_seller,
        )

    def test_user_has_information_fields(self):
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.password, self.password)
        self.assertEqual(self.user.first_name, self.first_name)
        self.assertEqual(self.user.last_name, self.last_name)
        self.assertEqual(self.user.is_seller, self.is_seller)