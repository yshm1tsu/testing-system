from django.contrib import admin
from .models import *


# Register your models here.

class Test2(admin.ModelAdmin):
     search_fields = ["name"]

class Meta:
         model = Test2

admin.site.register(Test, Test2)
