from rest_framework.test import APITestCase
from notes.apps.account.models import User, UserProfile
from rest_framework import status
import json
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class UserTests(APITestCase):
    def test_create_user(self):
        data = {
            "e_mail": "test@test.com",
            "password": "testpassword",
        }


        response = self.client.post('/api/users/', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_request_user(self):
        data = {
            "e_mail": "test1",
            "password": "1234",
        }

        response = self.client.post('/api/users/', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_request(self):
        data = {
            "e_mail": "test1@mail.com",
            "password": "",
        }

        response = self.client.post('/api/users/', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TokenTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(e_mail="test@test.com", password="testpassword")
        user.save()
        self.client = APIClient()

    def test_create_token(self):
        user = User.objects.get(e_mail="test@test.com")
        print Token.objects.get(user_id=user.id)

        response = self.client.post('/api/tokens/', {'e_mail': 'test@test.com', 'password':'testpassword'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_token(self):
        user = User.objects.get(e_mail="test@test.com")
        print Token.objects.get(user_id=user.id)

        response = self.client.post('/api/tokens/', {'e_mail': 'test', 'password':'testpassword'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(e_mail="test@test.com", password="testpassword")
        user.save()
        self.client = APIClient()
        self.client.login(e_mail="test@test.com", password="testpassword")
        # token = Token.objects.get(user__e_mail="test@test.com")
        # self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        # id = user.id
        profile = UserProfile.objects.create(first_name="nesto",
                                             last_name="neko",
                                             date_of_birth="2001-02-02",
                                             place="negde", state="nigde", user_id="1")
        profile.save()


    def test_update_profile(self):
        profile = {
            "first_name": "Ime",
                "last_name": "Prezime",
                "date_of_birth": "2001-02-02",
                "place": "mesto", "state": "drzava"
        }

        response = self.client.put('/api/users/{}/profile/'.format(id), json.dumps(profile),
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)







