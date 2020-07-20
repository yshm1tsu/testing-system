from django.db import models
import tests.helpers as helpers
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    text = models.TextField(verbose_name="Текст вопроса")
    answer = models.CharField(max_length=30, verbose_name="Ответ")
    points = models.IntegerField(default=0, verbose_name="Количество баллов за вопрос")
    with_options = models.BooleanField(verbose_name="С вариантами ответа")

class Test(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название теста")
    evaluated = models.BooleanField(verbose_name="Оцениваемый")
    questions_quantity = models.IntegerField(verbose_name="Количество вопросов")
    passed_quantiry = models.IntegerField(verbose_name="Количество прошедших")
    code = models.CharField(max_length=5, default=helpers.random_code, verbose_name="Код")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True, verbose_name="Автор")
