from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # admin panel
    url(r'^admin/', include(admin.site.urls)),

    # REST API
    url(r'^api/', include('notes.apps.auth.urls')),
    url(r'^api/notes/', include('notes.apps.writer.urls')),
]