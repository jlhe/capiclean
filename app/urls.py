from django.urls import path, include, re_path
from app.views import *
from . import views
from . import forms

urlpatterns = [
    path('',views.index, name="index"),
    path('login', views.login, name="Login"),
    path('ServicesList', views.editservices, name="List Services"),
    path('EditServices/<int:pk>', views.edit_service_details, name="Edit Services"),
    path('services', views.service, name="Services"),
    path('choose', views.choose, name="Choose services"),
    path('about', views.about, name="About"),
    path('team', views.team, name="Team"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('InvoiceGenerator', views.invoice_generator, name="Invoice Generator"),
]