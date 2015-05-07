from notes.apps.account import api
from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/$', api.Register.as_view()),
    url(r'^users/(?P<id>[0-9]+)/profile/$', api.UpdateProfile.as_view()),
    url(r'^tokens/$', api.TokenView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)