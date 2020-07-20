from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_creating, name='test_creating'),
]
