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
        #create notebook

        data = {
            'name':'Sve',
        }

        response = self.client.post(reverse('notebook_list'), json.dumps(data), content_type= 'application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_bad_request_create_notebook(self):
        #bad request for creating notebook

        data = {
            'name':''
        }

        response = self.client.post(reverse('notebook_list'),
                                    json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_get_notebooks(self):
        #read all notebooks

        notebook = Notebook.objects.create(name='nesto', user_id='1')
        notebook.save()
        notebook1 = Notebook.objects.create(name='ad', user_id='1')
        notebook1.save()

        response = self.client.get(reverse('notebook_list'), content_type = 'application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_no_notebooks(self):
        #there isn't any notebook

        response = self.client.get(reverse('notebook_list'), content_type = 'application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_notebook(self):
        #delete notebook with id

        notebook = Notebook.objects.create(name='nesto', user_id = '1')
        notebook.save()
        id = notebook.id

        response = self.client.delete(reverse('notebook_detail', args=[id]),
                                      content_type= 'application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_no_notebook(self):
        #delete non-existent

        response = self.client.delete(reverse('notebook_detail', args=[1]),
                                      content_type= 'application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



class NoteTests(APITestCase):


    def setUp(self):
        user = User.objects.create_user(username='nemanja', email='nesto@gmail', password='top_secret')
        user.save()
        self.client = APIClient()
        response = self.client.login(username = "nemanja", password = "top_secret")
        # print response


    def test_create_note(self):
        #create note in notebook

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        id = notebook.id

        data = {
            'title':'ASDAS',
            'contents': 'afaf', }

        response = self.client.post(reverse('note_list', args=[id]),
                                    json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_bad_create_note(self):
        #bad request for creating note

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        id = notebook.id

        data = {
            'title':'',
            'contents': 'addfs', }


        response = self.client.post(reverse('note_list', args=[id]),
                                    json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_no_notebook_note(self):
        #creating note in a non-existent notebook

        data = {
            'title':'ASDAS',
            'contents': 'afaf', }

        response = self.client.post(reverse('note_list', args=[1]),
                                    json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_all_notes(self):
        #get all notes from notebook with id

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        id = notebook.id
        note = Note.objects.create(title = 'beleska', contents = 'adasdasd', notebook_id = id)
        note.save()

        response = self.client.get(reverse('note_list', args=[id]), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_no_notes(self):
        #empty notebook,no notes

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        id = notebook.id

        response = self.client.get(reverse('note_list', args=[id]), content_type= 'application/json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_all_notes_no_notebook(self):
        #get notes from non-existent notebook

        note = Note.objects.create(title = 'beleska', contents = 'adasdasd', notebook_id = '28')
        note.save()

        response = self.client.get(reverse('note_list', args=[1]), content_type= 'application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_update_note(self):
        #update note with id in notebook_id

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        notebook_id = notebook.id
        note = Note.objects.create(title = 'beleska', contents = 'adasdasd', notebook_id = notebook_id)
        note.save()
        id = note.id

        data = {
            'title':'ASDAS',
            'contents': 'afaf', }

        response = self.client.put(reverse('note_detail', args=[notebook_id, id]),
                                   json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_bad_update_note(self):
        # bad update note

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        notebook_id = notebook.id
        note = Note.objects.create(title = 'beleska', contents = 'adasdasd', notebook_id = notebook_id)
        note.save()
        id = note.id

        data = {
            'title':'',
            'contents': 'afaf', }

        response = self.client.put(reverse('note_detail', args=[notebook_id, id]),
                                   json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_update_no_note(self):
        #update non-existent note

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        notebook_id = notebook.id

        data = {
            'title':'ASDAS',
            'contents': 'afaf', }

        response = self.client.put(reverse('note_detail', args=[notebook_id, 1]),
                                   json.dumps(data), content_type = 'application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_note(self):
        #delete note with id

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        notebook_id = notebook.id
        note = Note.objects.create(title = 'beleska', contents = 'adasdasd', notebook_id = notebook_id)
        note.save()
        id = note.id

        response = self.client.delete(reverse('note_detail',
                                              args=[notebook_id, id]), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_delete_no_note(self):
        #delete non-existent note

        notebook = Notebook.objects.create(name = 'nesto', user_id = '1')
        notebook.save()
        notebook_id = notebook.id

        response = self.client.delete(reverse('note_detail',
                                              args=[notebook_id, id]), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)














