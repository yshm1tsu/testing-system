from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from tests.forms import SignUpForm, CreateTestForm

from tests.models import Test

def index(request):
    if request.user.is_authenticated:
        return redirect('cabinet')

    return render(request, 'tests/index.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'tests/register.html', context)

def logout(request):
    auth_logout(request)
    return redirect('index')

@login_required
def cabinet(request):
    test_list = Test.objects.filter(author=request.user)
    context = {'test_list': test_list}
    return render(request, 'tests/cabinet.html', context)

@login_required
def create_test(request):
    form = CreateTestForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            newTest = form.save(commit=False)
            newTest.author = request.user
            newTest.save()
            return redirect('cabinet')

    context = {'form': form}
    return render(request, 'tests/createTest.html', context)
