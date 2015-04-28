from notes.apps.account import api
from django.conf.urls import url

urlpatterns = [
    url(r'^users/$', api.CreateUser.as_view()),
    url(r'^users/(?P<id>[0-9]+)/profile/$', api.UpdateProfile.as_view()),
    ]
