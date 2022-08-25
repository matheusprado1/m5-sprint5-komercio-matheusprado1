from rest_framework.test import APITestCase

from accounts.models import Account
from ..models import Product


class UsersViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = {
            'description': 'Patinete sem roda',
            'price': 12.50,
            'quantity': 1,
        }

        cls.wrong_product = {
            'price': 12.50,
            'quantity': 1,
        }

        cls.wrong_product_negative = {
            'description': 'Patinete sem roda',
            'price': 12.50,
            'quantity': -1,
        }

        cls.user_buyer = {
            'username': 'jorel',
            'password': '1234',
            'first_name': 'Irmão',
            'last_name': 'Jorel',
            'is_seller': False,
        }

        cls.user_seller = {
            'username': 'jorel',
            'password': '1234',
            'first_name': 'Irmão',
            'last_name': 'Jorel',
            'is_seller': True,
        }

    def test_seller_create_product(self):

        self.client.post('/api/accounts/', self.user_seller, format='json')

        login_data = {
            'username': self.user_seller['username'],
            'password': self.user_seller['password']
        }

        auth = self.client.post('/api/login/', login_data, format='json')

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + auth.data['token']
        )

        response = self.client.post(
            '/api/products/',
            self.product,
            format='json'
        )

        self.assertEquals(response.status_code, 201)
        self.assertTrue(response.data["seller"])

    def test_buyer_create_product(self):

        self.client.post('/api/accounts/', self.user_buyer, format='json')

        login_data = {
            'username': self.user_seller['username'],
            'password': self.user_seller['password']
        }

        auth = self.client.post('/api/login/', login_data, format='json')

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + auth.data['token']
        )

        response = self.client.post(
            '/api/products/',
            self.product,
            format='json'
        )

        self.assertEquals(response.status_code, 403)
        self.assertEqual(response.data, {
            'detail': 'You do not have permission to perform this action.'
        },)

    def test_seller_create_product_with_wrong_keys(self):

        self.client.post('/api/accounts/', self.user_seller, format='json')

        login_data = {
            'username': self.user_seller['username'],
            'password': self.user_seller['password'],
        }

        auth = self.client.post('/api/login/', login_data, format='json')

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + auth.data['token']
        )

        response = self.client.post(
            '/api/products/',
            self.wrong_product,
            format='json',
        )

        self.assertEquals(response.status_code, 400)
        self.assertTrue(response.data['description'])

    def test_list_products(self):

        response = self.client.get("/api/products/")
        self.assertEquals(response.status_code, 200)

    def test_negative_product(self):

        self.client.post('/api/accounts/', self.user_seller, format='json')

        login_data = {
            'username': self.user_seller['username'],
            'password': self.user_seller['password'],
        }

        auth = self.client.post('/api/login/', login_data, format='json')

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + auth.data['token']
        )

        response = self.client.post(
            '/api/products/',
            self.wrong_product_negative,
            format='json',
        )

        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data['quantity'][0],
                          'Ensure this value is greater than or equal to 0.',
                          )
