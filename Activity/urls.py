from django.urls import re_path
from Activity import views

urlpatterns = [
    re_path(r'^(\d+)$', views.activity, name='activity'),
    re_path(r'^activity_detail/(\d+)$', views.activity_detail, name="activity_detail"),
    re_path(r'^enter$', views.enter, name="enter"),
    re_path(r'^enter_success$', views.enter_success, name='enter_success'),
]
