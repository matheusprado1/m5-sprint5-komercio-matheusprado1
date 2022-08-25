from rest_framework.test import APITestCase
from accounts.models import Account


class UsersViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.username = 'tarobinha'
        cls.password = '12345'
        cls.first_name = 'taroba'
        cls.last_name = 'oliveira'
        cls.is_seller = True

        cls.user_seller = {
            'username': 'jorel',
            'password': '1234',
            'first_name': 'Irmão',
            'last_name': 'Jorel',
            'is_seller': True,
        }

        cls.user_buyer = Account.objects.create(
            username=cls.username,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=cls.is_seller,
        )

    def test_post_a_seller(self):

        user_1 = {
            'username': 'jorel',
            'password': '1234',
            'first_name': 'Irmão',
            'last_name': 'Jorel',
            'is_seller': True,
        }

        response = self.client.post('/api/accounts/', data=user_1)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['is_seller'])

    def test_post_a_buyer(self):

        user_1 = {
            'username': 'math',
            'password': '1234',
            'first_name': 'Matheus',
            'last_name': 'Prado',
            'is_seller': False,
        }

        response = self.client.post('/api/accounts/', data=user_1)

        self.assertEqual(response.status_code, 201)
        self.assertFalse(response.data['is_seller'])

    def test_post_a_wrong_data(self):

        user_1 = {
            'username': 'math',
            'password': '1234',
            'last_name': 'Prado',
            'is_seller': False,
        }

        response = self.client.post('/api/accounts/', data=user_1)

        self.assertEqual(response.status_code, 400)

    def test_login_generate_token(self):

        self.client.post('/api/accounts/', self.user_seller, format='json')

        login_data = {
            'username': self.user_seller['username'],
            'password': self.user_seller['password'],
        }

        response = self.client.post('/api/login/', login_data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['token'])

    def test_get_users(self):

        response = self.client.get('/api/accounts/')

        self.assertEqual(response.status_code, 200)