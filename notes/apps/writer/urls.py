from notes.apps.writer import api
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^$', api.NotebookList.as_view()),
    url(r'^(?P<notebook_id>[0-9]+)/$', api.NotebookDetail.as_view()),
    url(r'^(?P<notebook_id>[0-9]+)/notes/$', api.NoteList.as_view()),
    url(r'^(?P<notebook_id>[0-9]+)/notes/(?P<id>[0-9]+)/$', api.NoteDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)