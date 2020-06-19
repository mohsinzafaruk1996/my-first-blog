from django.conf.urls import url
from . import views
from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]


