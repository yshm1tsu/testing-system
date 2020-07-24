from django.contrib import admin
from .models import Test, Question, Option, Result

admin.site.register(Option)

class ResultAdmin(admin.TabularInline):
    model = Result

class QuestionAdmin(admin.TabularInline):
    model = Question
    fields = ('text', 'points')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'author')
    inlines = (QuestionAdmin, ResultAdmin)
