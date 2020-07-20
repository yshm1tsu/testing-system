from django.shortcuts import render
from .forms import TestForm, QuestionForm

# Create your views here.
def test_creating(request):
   test = TestForm(request.POST or None)
   question = QuestionForm(request.POST or None)
   if request.method == "POST" :
        test = test.save()
   return render(request, 'tests/test_creating.html',locals())

