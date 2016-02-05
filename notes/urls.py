from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # admin panel
    url(r'^admin/', include(admin.site.urls)),

    # REST API
    url(r'^api/', include('notes.apps.account.urls')),
    url(r'^api/notebooks/', include('notes.apps.writer.urls')),
    url(r'^api/tasks/', include('notes.apps.tasks.urls')),

    # swagger
    url(r'^swagger/', include('rest_framework_swagger.urls')),
]
