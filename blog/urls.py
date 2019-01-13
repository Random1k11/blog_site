from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    path('text/', views.text, name='tetx')
]
