from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from notes.apps.writer import api


urlpatterns = [

    url(r'^$', api.NotebookList.as_view(), name='notebook_list'),
    url(r'^(?P<notebook_id>[0-9]+)/$', api.NotebookDetail.as_view(), name='notebook_detail'),
    url(r'^(?P<notebook_id>[0-9]+)/notes/$', api.NoteList.as_view(), name='note_list'),
    url(r'^(?P<notebook_id>[0-9]+)/notes/(?P<id>[0-9]+)/$', api.NoteDetail.as_view(), name='note_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)