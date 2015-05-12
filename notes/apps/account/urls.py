from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from notes.apps.account import api


urlpatterns = [
    url(r'^users/$', api.Register.as_view(), name='register'),
    url(r'^users/(?P<id>[0-9]+)/profile/$', api.UpdateProfile.as_view(), name='profile'),
    url(r'^tokens/$', api.TokenView.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

