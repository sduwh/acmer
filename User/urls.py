from django.urls import re_path
from User import views

urlpatterns = [
    re_path(r'^center$', views.user, name="user_center"),
    re_path(r'^change$', views.user_info_change, name="user_info_change"),
    re_path(r'^user_logout$', views.user_logout, name="user_logout"),
    re_path(r'^user_login$', views.user_login, name="user_login"),
    re_path(r'^user_register$', views.register, name="user_register"),
    re_path(r'^sso_auth$', views.sso_auth, name='sso_auth'),
    re_path(r'^sso_login$', views.sso_login, name='sso_login')
]
