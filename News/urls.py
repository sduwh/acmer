from django.urls import re_path
from News import views

urlpatterns = [
    re_path(r'^$', views.news, name='news'),
    re_path(r'^news_detail/(\d+)$', views.news_detail, name='news_detail'),
    re_path(r'^more/(\S+)/(\d+)$', views.news_more, name='news_more')
]
