from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from index.views import email_create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    # path('create/', email_create)
]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]

urlpatterns += staticfiles_urlpatterns()
