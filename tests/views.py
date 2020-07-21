from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from tests.forms import SignUpForm, CreateTestForm
from tests.models import Test, Question, Option

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
            newTest = Test()
            newTest.author = request.user
            newTest.name = request.POST['name']
            newTest.save()

            max_question_index = request.POST.get('max_question_index')
            for i in range(int(max_question_index)):
                if request.POST.get('question_title_' + str(i), False):
                    question = Question()
                    question.test = newTest
                    question.text = request.POST['question_title_' + str(i)]
                    question.points = request.POST['question_points_' + str(i)]
                    question.save()
                    max_option_index = request.POST['question_form_options_index_' + str(i)]
                    for j in range(int(max_option_index)):
                        if request.POST.get('question_option_' + str(i) + '_' + str(j), False):
                            option = Option()
                            option.question = question
                            option.text = request.POST['question_option_' + str(i) + '_' + str(j)]
                            option.is_correct = bool(request.POST.get('question_option_is_correct_' + str(i) + '_' + str(j)))
                            option.save()

            return redirect('cabinet')

    context = {'form': form}
    return render(request, 'tests/createTest.html', context)

@login_required
def delete_test(request):
    try:
        test = Test.objects.get(code=request.GET['code'], author=request.user)
        test.delete()
    except:
        return redirect('index')

    return redirect('cabinet')

