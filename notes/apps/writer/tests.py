from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import json
from django.contrib.auth import get_user_model
from notes.apps.writer.models import Note, Notebook
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token


User = get_user_model()

class NotebookTests(APITestCase):


    def setUp(self):
        user = User.objects.create_user(e_mail='nesto@mail', password='top_secret')
        user.save()
        self.client = APIClient()
        token = Token.objects.get(user_id=user.id)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    def test_create_notebook(self):
        """Create notebook"""


        data = {
            'name':'Sve',
        }

        response = self.client.post(reverse('notebook_list'), json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_notebook_bad_request(self):
        """Bad request for creating notebook"""

        data = {
            'name':''
        }

        response = self.client.post(reverse('notebook_list'),
                                    json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_get_notebooks(self):
        """Read all notebooks"""

        notebook = Notebook.objects.create(name='nesto', user_id='1')
        notebook.save()
        notebook1 = Notebook.objects.create(name='ad', user_id='1')
        notebook1.save()

        response = self.client.get(reverse('notebook_list'), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_no_notebooks(self):
        """There isn't any notebook"""

        response = self.client.get(reverse('notebook_list'), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_notebook(self):
        """Delete notebook with notebook_id"""

        notebook = Notebook.objects.create(name='nesto', user_id='1')
        notebook.save()
        id = notebook.id

        response = self.client.delete(reverse('notebook_detail', args=[id]),
                                      content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_no_notebook(self):
        """Delete non-existent notebook"""

        response = self.client.delete(reverse('notebook_detail', args=[1]),
                                      content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



class NoteTests(APITestCase):


    def setUp(self):
        self.user = User.objects.create_user(e_mail='nesto@gmail', password='top_secret')
        self.notebook = Notebook.objects.create(name='dummy', user=self.user)

        self.client = APIClient()

    def test_create_note(self):
        """Create note in notebook with notebook_id"""
        id = self.notebook.id

        data = {
            'title':'ASDAS',
            'contents':'afaf',
        }

        response = self.client.post(reverse('note_list', args=[id]),
                                    json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_note_bad_request(self):
        """Bad request for creating note"""

        id = self.notebook.id

        data = {
            'title':'',
            'contents':'addfs',
            }


        response = self.client.post(reverse('note_list', args=[id]),
                                    json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_no_notebook_note(self):
        """Creating note in a non-existent notebook"""

        data = {
            'title':'ASDAS',
            'contents':'afaf',
            }

        response = self.client.post(reverse('note_list', args=[1]),
                                    json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_all_notes(self):
        """Get all notes from notebook with notebook_id"""

        id = self.notebook.id
        note = Note.objects.create(title='beleska', contents='adasdasd', notebook_id=id)
        note.save()

        response = self.client.get(reverse('note_list', args=[id]), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_no_notes(self):
        """Empty notebook,no notes"""

        id = self.notebook.id

        response = self.client.get(reverse('note_list', args=[id]), content_type='application/json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_all_notes_no_notebook(self):
        """Get notes from non-existent notebook"""

        note = Note.objects.create(title='beleska', contents='adasdasd', notebook_id='28')
        note.save()

        response = self.client.get(reverse('note_list', args=[1]), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_update_note(self):
        """Update note with id in notebook_id"""

        notebook_id =self.notebook.id
        note = Note.objects.create(title='beleska', contents='adasdasd', notebook_id=notebook_id)
        note.save()
        id = note.id

        data = {
            'title':'ASDAS',
            'contents':'afaf',
            }

        response = self.client.put(reverse('note_detail', args=[notebook_id, id]),
                                   json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_bad_update_note(self):
        """Bad update note"""

        notebook_id = self.notebook.id
        note = Note.objects.create(title='beleska', contents='adasdasd', notebook_id=notebook_id)
        note.save()
        id = note.id

        data = {
            'title':'',
            'contents':'afaf',
            }

        response = self.client.put(reverse('note_detail', args=[notebook_id, id]),
                                   json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_update_no_note(self):
        """Update non-existent note"""

        notebook_id = self.notebook.id

        data = {
            'title':'ASDAS',
            'contents':'afaf',
            }

        response = self.client.put(reverse('note_detail', args=[notebook_id, 1]),
                                   json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_note(self):
        """Delete note with id"""

        notebook_id = self.notebook.id
        note = Note.objects.create(title='beleska', contents='adasdasd', notebook_id=notebook_id)
        note.save()
        id = note.id

        response = self.client.delete(reverse('note_detail',
                                              args=[notebook_id, id]), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_delete_no_note(self):
        """Delete non-existent note"""

        notebook_id = self.notebook.id

        response = self.client.delete(reverse('note_detail',
                                              args=[notebook_id, "1"]), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)














