from django.urls import path
from . import views
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.home, name='home',)
]
