import json

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from notes.apps.account.models import User, UserProfile


class UserTests(APITestCase):
    def test_create_user(self):
        data = {
            "e_mail": "test@test.com",
            "password": "testpassword",
        }

        response = self.client.post(reverse('register'), json.dumps(data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_request_user(self):
        data = {
            "e_mail": "test1",
            "password": "1234",
        }

        response = self.client.post(reverse('register'), json.dumps(data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_request(self):
        data = {
            "e_mail": "test1@mail.com",
            "password": "",
        }

        response = self.client.post(reverse('register'), json.dumps(data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TokenTests(APITestCase):
    def setUp(self):
        User.objects.create_user(e_mail="test@test.com", password="testpassword")
        self.client = APIClient()

    def test_create_token(self):
        User.objects.get(e_mail="test@test.com")

        response = self.client.post(reverse('login'),
                                    {'e_mail': 'test@test.com', 'password': 'testpassword'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_token(self):
        User.objects.get(e_mail="test@test.com")

        response = self.client.post(reverse('login'),
                                    {'e_mail': 'test', 'password': 'testpassword'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(e_mail="test@test.com", password="testpassword")
        self.client = APIClient()

    def test_update_profile(self):
        self.client.login(e_mail="test@test.com", password="testpassword")
        token = Token.objects.get(user=self.user.id)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        profile = {
            "first_name": "Ime",
            "last_name": "Prezime",
            "place": "mesto",
            "state": "drzava",
        }

        response = self.client.put(reverse('profile', args=[self.user.id]), json.dumps(profile),
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user_profile = UserProfile.objects.get(user=self.user.id)

        for field, value in profile.iteritems():
            db_value = getattr(user_profile, field)
            self.assertEqual(db_value, value)

    def test_unauthorized_profile(self):
        self.client.login(e_mail="test@test.com", password="testpassword")

        profile = {
            "first_name": "Ime",
            "last_name": "Prezime",
            "date_of_birth": "2001-02-02",
            "place": "mesto",
            "state": "drzava",
        }

        response = self.client.put(reverse('profile', args=[self.user.id]), json.dumps(profile),
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_bad_request_profile(self):
        self.client.login(e_mail="test@test.com", password="testpassword")
        token = Token.objects.get(user=self.user.id)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        profile = {
            "first_name": "Ime",
            "last_name": "Prezime",
            "date_of_birth": "02-01-2002",
            "place": "mesto",
            "state": "drzava",
        }

        response = self.client.put(reverse('profile', args=[self.user.id]), json.dumps(profile),
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)





