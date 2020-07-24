from django.urls import path
from django.contrib.auth import views as auth_views
from tests.forms import LoginForm
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='tests/login.html', authentication_form=LoginForm), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('createTest/', views.create_test, name='create_test'),
    path('deleteTest/', views.delete_test, name='delete_test'),
    path('validateCreateTest/', views.validate_create_test, name='validate_create_test'),
    path('passTest/<str:code>', views.pass_test, name='pass_test'),
    path('result/<str:code>', views.result, name='result')
]
