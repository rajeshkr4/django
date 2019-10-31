from django.contrib import  admin
from django.urls import path
from .views import registeruser


urlpatterns = [
    path('register',registeruser),
]