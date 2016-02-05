from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from notes.apps.tasks import api


urlpatterns = [
    url(r'^$', api.TaskList.as_view(), name='task_list'),
    url(r'^(?P<asigned_to>[^@]+@[^@]+\.[^@]+)/$', api.UserTasks.as_view(), name='user_task_list'),
    url(r'^(?P<task_id>[0-9]+)/tasks$', api.TaskDetail.as_view(), name='task_status'),
    url(r'^(?P<task_id>[0-9]+)/comments/$', api.CommentList.as_view(), name='comment_list'),
    url(r'^(?P<task_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$', api.CommentDetail.as_view(), name='comment_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
