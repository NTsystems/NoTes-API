from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # admin panel
    url(r'^admin/', include(admin.site.urls)),

    # REST API
    url(r'^api/', include('notes.apps.account.urls')),
    # url(r'^api/notebooks/', include('notes.apps.writer.urls')),
]
