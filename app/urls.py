from django.urls import path, include, re_path
from app.views import *
from . import views
from . import forms

urlpatterns = [
    path('',views.index, name="index"),
    path('login', views.login, name="Login"),
    path('ServicesList', views.editservices, name="List Services"),
    path('EditServices/<int:pk>', views.edit_service_details, name="Edit Services")
]