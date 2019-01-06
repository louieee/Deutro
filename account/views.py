from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'account/login.html')


def signup(request):
    return render(request, 'account/signup.html')


def logout(request):
    return render(request, 'home.html')


def signup_teacher(request):
    return render(request, 'account/signup_teacher.html')


def signup_student(request):
    return render(request, 'account/signup_student.html')
