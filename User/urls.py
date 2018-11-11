from django.urls import re_path
from User import views

urlpatterns = [
    re_path(r'^center$', views.user, name="user_center"),
    re_path(r'^user_logout$', views.user_logout, name="user_logout"),
    re_path(r'^user_login$', views.user_login, name="user_login"),
    re_path(r'^user_register$', views.register, name="user_register"),
]
