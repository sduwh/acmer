from django.urls import re_path
from Team import views

urlpatterns = [
    re_path(r'^join_us$', views.join_us, name='join_us'),
    re_path(r'^history$', views.history, name='history'),
]
