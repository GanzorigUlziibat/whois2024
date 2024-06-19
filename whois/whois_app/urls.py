from django.contrib import admin
from django.urls import path
from whois_app.views import index, home

urlpatterns = [
    path('', home, name='home')
]
