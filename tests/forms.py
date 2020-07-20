from django import forms
from .models import *

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ["passed_quantiry"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = [""]
