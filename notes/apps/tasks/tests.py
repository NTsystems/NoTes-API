import json
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from notes.apps.tasks.models import Task, Comment


class TaskTests(APITestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.create_user(e_mail='user1@gmail.com', password='123')
        self.user1.is_active = True
        self.user1.save(update_fields=['is_active'])
        self.user2 = get_user_model().objects.create_user(e_mail='user2@gmail.com', password='1233456')
        self.user2.is_active = True
        self.user2.save(update_fields=['is_active'])
        self.client = APIClient()
        token = Token.objects.get(user_id=self.user1.id)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    def test_create_task(self):
        """Create task test"""
        data = {
                'name': 'task1',
                'asigned_to': 1,
                'status': 1,
                'description': 'opis task',
                'status': 1
        }
        response = self.client.post(reverse('task_list'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_task_bad_request(self):
        """Creating task bad request"""
        data = {
                'name': '',

                'status': 1,
                'description': 'opis task',
                'status': 1
        }
        response = self.client.post(reverse('task_list'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_tasks(self):
        """No created tasks"""
        response = self.client.get(reverse('task_list'), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_tasks(self):
        """Get all tasks"""
        Task.objects.create(name='task1', asigned_to=self.user1, description='opis1', status=1)
        Task.objects.create(name='task2', asigned_to=self.user1, description='opis2', status=1)

        response = self.client.get(reverse('task_list'), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_assigned_to_bad_request(self):
        """User trying to see task he's assigned to(no tasks)"""
        Task.objects.create(name='task1', asigned_to=self.user1, description='opis1', status=1)
        Task.objects.create(name='task2', asigned_to=self.user1, description='opis2', status=1)

        response = self.client.get(reverse('user_task_list', args=[self.user2.id]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_task_assigned_to(self):
        """User trying to see task he's assigned to"""
        Task.objects.create(name='task1', asigned_to=self.user1, description='opis1', status=1)
        Task.objects.create(name='task2', asigned_to=self.user1, description='opis2', status=1)

        response = self.client.get(reverse('user_task_list', args=[self.user1.id]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task_status(self):
        """Updates status"""
        task = Task.objects.create(name='task', asigned_to=self.user1, description='opis1', status=1)
        data = {
                'name': 'task',
                'asigned_to': 'self.user1',
                'desription': 'promenjen opis',
                'status': '2'
        }

        response = self.client.put(reverse('task_status', args=[task.id]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task_status_bad_request(self):
        """Bad status update"""
        task = Task.objects.create(name='task', asigned_to=self.user1, description='opis1', status=1)
        data = {
                'name': 'task',
                'asigned_to': 'self.user1',
                'desription': 'promenjen opis',
                'status': '10'  # status moze biti samo 1,2,3,4
        }

        response = self.client.put(reverse('task_status', args=[task.id]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CommentTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(e_mail='user@user.com', password='userpass')
        self.user.is_active = True
        self.user.save(update_fields=['is_active'])
        self.task = Task.objects.create(name='task1', asigned_to=self.user, description='opis1', status=1)
        self.client = APIClient()
        token = Token.objects.get(user_id=self.user.id)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    def test_post_comment(self):
        """Creating comment for specific task"""
        data = {
                'text': "Some non important comment"
        }
        response = self.client.post(reverse('comment_list', args=[self.task.id]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_comment_for_non_existing_task(self):
        """Creating comment for non existing task"""
        data = {
                'text': "Some not important comment"
        }
        response = self.client.post(reverse('comment_list', args=[25]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_all_comments_for_specific_task(self):
        """Get all available comments for specific task"""
        Comment.objects.create(text='blabla', task=self.task)
        response = self.client.get(reverse('comment_list', args=[self.task.id]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_comments_invalid_taskid(self):
        """Get all available comments for non existing task"""
        Comment.objects.create(text='blabla', task=self.task)
        response = self.client.get(reverse('comment_list', args=[25]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_specific_comment(self):
        """Get specific comment"""
        com1 = Comment.objects.create(text='blabla1', task=self.task)

        response = self.client.get(reverse('comment_detail', args=[self.task.id, com1.id]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_comment_dont_exist(self):
        """Get specific comment"""

        response = self.client.get(reverse('comment_detail', args=[self.task.id, 123]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_comment(self):
        """Delete comment"""
        com1 = Comment.objects.create(text='blabla1', task=self.task)
        response = self.client.delete(reverse('comment_detail', args=[self.task.id, com1.id]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_comment_bad_request(self):
        """Delete non existing comment"""

        response = self.client.delete(reverse('comment_detail', args=[self.task.id, 23]), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Authorization(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(e_mail='stefan@gmail.com', password='stefan')
        self.user.is_active = True
        self.user.save(update_fields=['is_active'])
        self.task = Task.objects.create(name='task1', asigned_to=self.user, description='opis1', status=1)
        self.client = APIClient()

    def test_create_task_no_authorization(self):
        """Creating task without authorization"""
        data = {
                'name': 'task1',
                'asigned_to': 1,
                'status': 1,
                'description': 'opis task',
                'status': 1
        }

        response = self.client.post(reverse('task_list', args=[self.task.id]), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
