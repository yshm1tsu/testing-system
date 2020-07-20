from django.shortcuts import render, redirect
from tests.forms import SignUpForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from tests.forms import SignUpForm
from django.contrib.auth.decorators import login_required

def index(request):
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
    return render(request, 'tests/cabinet.html')
