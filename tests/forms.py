from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from tests import models

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        label='Пароль',
        max_length=30,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        label='Повторите пароль',
        max_length=30,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    error_messages = {
        'password_mismatch': 'Пароли должны совпадать'
    }

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Имя пользователя',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        label='Пароль',
        max_length=30,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    error_messages = {
        'invalid_login': 'Неверное имя пользователя или пароль'
    }

    class Meta:
        model = User
        fields = ('username', 'password')

class CreateTestForm(forms.ModelForm):

    name = forms.CharField(
        label='Название теста',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    # evaluated = forms.BooleanField(
    #     label='С баллами',
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             "class": "form-check-input"
    #         }
    #     )
    # )

    class Meta:
        model = models.Test
        exclude = ["code", "author", "evaluated"]
