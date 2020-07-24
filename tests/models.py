from django.db import models
import tests.helpers as helpers
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

class Test(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название теста")
    code = models.CharField(max_length=5, default=helpers.random_code, verbose_name="Код")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True, verbose_name="Автор")

    def __str__(self):
        return self.name
    

class Question(models.Model):
    test = models.ForeignKey(Test,on_delete=models.CASCADE, null = True, verbose_name = "Тест")
    text = models.TextField(verbose_name="Текст вопроса")
    points = models.IntegerField(default=0, verbose_name="Количество баллов за вопрос")

    def __str__(self):
        return self.text
    


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null = True, verbose_name = "Вопрос")
    text = models.CharField(max_length = 30, verbose_name = "Текст")
    is_correct = models.BooleanField(verbose_name = "Корректность")

    def __str__(self):
        return self.text
    

class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null = True, verbose_name = "Тест")
    name = models.CharField(max_length = 20, verbose_name = "Имя")
    total_points = models.IntegerField(default = 0, verbose_name = "Баллы")
    date = models.DateTimeField(default=timezone.now, blank = True, verbose_name = "Дата")

    def __str__(self):
        return self.name
    
