from notes.apps.writer import api
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^$', api.NotebookList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', api.NotebookDetail.as_view()),
    url(r'^(?P<pk>[0-9]+)/notes/$', api.NoteList.as_view()),
    #url(r'^(?P<pk>[0-9]+)/notes/(?P<pk>[0-9]+)$', api.NoteList.NoteDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)