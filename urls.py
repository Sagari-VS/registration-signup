from django.conf.urls import include
from django.urls import path
from . import views
from .views import successpage
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
   path('formnew/', views.contact),
   # path('register/', views.post),
   #path('login/', views.login),
   path('loginview/', views.loginview),
   #path('contactview/', views.ContactView),
   path('list/', successpage, name='successpage'),

]

