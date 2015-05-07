from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import json
from django.contrib.auth.models import User
from notes.apps.writer.models import Note, Notebook
from django.core.urlresolvers import reverse


class NotebookTests(APITestCase):

    def setUp(self):
        user = User.objects.create_user( username='nemanja', email='nesto@mail', password='top_secret')
        user.save()
        self.client = APIClient()
        response = self.client.login(username="nemanja", password="top_secret" )


    def test_create_notebook(self):
        data = {
            'name':'Sve',
        }

        response = self.client.post('/api/notebooks/', json.dumps(data), content_type= 'application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_request_create_notebook(self):
        data = {
            'name':''
        }
        url = '/api/notebooks/'

        response = self.client.post(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_notebooks(self):

        # data = {
        #     "name":"nesto"
        # }

        url = '/api/notebooks/'

        response = self.client.get(url, content_type = 'application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)




# class NoteTests(APITestCase):
#
#     def setUp(self):
#         user = User.objects.create_user(username='nemanja', email='nesto@gmail', password='top_secret')
#         user.save()
#         notebook = Notebook.objects.create(name = 'nesto')
#         notebook.save()
#         id = notebook.id
#         self.client = APIClient
#         response = self.client.login(username = "nemanja", password = "top_secret")
#         print response

    # def test_get_note_id(self):
    #     data = {
    #         "id" : 5,
    #         'title':'ASDAS',
    #         'contents': 'afaf', }
    #
    #     response = self.client.get('/api/notebooks/9/notes/5/', json.dumps(data), content_type = 'application/json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_note(self):
    #
    #     data = {
    #         "title": "beleska",
    #         "contents": "dasdasd",
    #     }
    #
    #     response = self.client.post('api/notebooks/{}/notes'.format(id), json.dumps(data), content_type= 'application/json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)