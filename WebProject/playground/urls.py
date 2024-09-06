from django.urls import path
from . import views

urlpatterns = [
    path('playground/hi/', views.greeting)
]