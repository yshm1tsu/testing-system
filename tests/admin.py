from django.contrib import admin
from .models import *

class TestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Test, TestAdmin)
