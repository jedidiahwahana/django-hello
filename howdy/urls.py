# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
               url(r'^$', views.HomePageView.as_view()),
               url(r'^callback$', views.callback, name='callback'),
               url(r'^hello$', views.hello, name='hello')
               ]
