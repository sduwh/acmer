from django.urls import re_path
from codePool import views

urlpatterns = [
    re_path(r'^(\d+)$', views.code_pool, name='code_pool'),
    re_path(r'^my/(\d+)$', views.my_code_pool, name='code_pool_index'),
    re_path(r'^detail/(\d+)$', views.code_detail, name='code_detail'),
    re_path(r'^change/(\d+)$', views.change_code, name='change_code'),
    re_path(r'^del/(\d+)$', views.del_code, name='del_code'),
    re_path(r'^create_code$', views.create_code, name='create_code')
]
