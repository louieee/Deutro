import re
from datetime import date

from django.contrib import auth
from django.shortcuts import render, redirect

from Utilities.custom_views import DefaultView
from school.models import School
from student.models import Student
from student.models import User
from subject.models import Subject
from teacher.models import Teacher


# Create your views here.
class LoginView(DefaultView):
    template = 'account/login.html'

    def post(self, request):
        username = str(request.POST.get('username', False))
        password = str(request.POST.get('password', False))
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error = 'Username or Password is Incorrect'
            return render(request, 'account/login.html', {'error': error, 'user': username, 'pass': password})


def signup(request):
    return render(request, 'account/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def signup_teacher(request):
    classes = get_class()
    if request.method == 'POST':
        fn = str(request.POST.get('firstname', False))
        ln = str(request.POST.get('lastname', False))
        subject = str(request.POST.get('subject', False))
        gender = str(request.POST.get('gender', False))
        gen = 1
        if gender == 'Male':
            gen = 1
        elif gender == 'Female':
            gen = 2
        prim = False
        sec = False
        school_level = str(request.POST.get('teacher', False))
        if school_level == 'Primary':
            prim = True
        elif school_level == 'Secondary':
            sec = True
        school = str(request.POST.get('school', False))
        class_ = str(request.POST.get('class', False))
        stage = int(class_[len(class_) - 1:])
        pass1 = str(request.POST.get('password1', False))
        pass2 = str(request.POST.get('password2', False))
        number = 1000 + int(Teacher.objects.all().count())
        username = get_username(school, str(number), 'T', fn, ln)
        if pass1 == pass2:
            try:
                error = 'User already exists'
                status = 'danger'
                user = User.objects.get(username=username)
                return render(request, 'account/signup_teacher.html',
                              {'error': error, 'status': status, 'schools': School.objects.all(),
                               'subjects': Subject.objects.all(), 'classes': classes})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=pass1, is_teacher=True)
                sch_id = int(School.objects.all().get(name=school).id)
                d_teacher = Teacher(School_id=sch_id, user=user, First_Name=fn, Last_Name=ln,
                                    Gender=gen, stage=stage, subject=subject)
                d_teacher.user.is_teacher = True
                d_teacher.save()
                message = 'Your Username is ' + username
                return render(request, 'home.html', {'message': message})
        else:
            error = 'Passwords must match'
            status = 'danger'
            return render(request, 'account/signup_teacher.html',
                          {'error': error, 'status': status, 'schools': School.objects.all(),
                           'subjects': Subject.objects.all(), 'classes': classes})
    else:
        pass
    return render(request, 'account/signup_teacher.html', {'schools': School.objects.all(),
                                                           'subjects': Subject.objects.all(), 'classes': classes})


def signup_student(request):
    classes = get_class()
    if request.method == 'POST':
        class_ = str(request.POST.get('stage', False))
        fn = str(request.POST.get('firstname', False))
        ln = str(request.POST.get('lastname', False))
        age = str(request.POST.get('age', False))
        stage = int(class_[len(class_) - 1:])
        dob = re.split('-', age)
        gender = str(request.POST.get('gender', False))
        gen = 1
        if gender == 'Male':
            gen = 1
        elif gender == 'Female':
            gen = 2

        entry_yr = str(request.POST.get('year', False))
        prim = False
        sec = False
        school_level = str(request.POST.get('school_level', False))
        if school_level == 'Primary':
            prim = True
        elif school_level == 'Secondary':

            sec = True

        school = str(request.POST.get('school', False))
        pass1 = str(request.POST.get('password1', False))
        pass2 = str(request.POST.get('password2', False))
        sch_id = int(School.objects.get(name=school).id)
        number = 7000 + int(Student.objects.all().count())
        username = get_username(school, str(number), 'S', fn, ln)
        if pass1 == pass2:
            try:
                error = 'User already exists'
                status = 'danger'
                user = User.objects.get(username=username)
                return render(request, 'account/signup_student.html',
                              {'error': error, 'classes': classes, 'status': status, 'schools': School.objects.all()})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=pass1, is_student=True)
                school = School.objects.all().get(name=school)
                d_student = Student(School_id=sch_id, user=user, First_Name=fn, Last_Name=ln, Entry_year=int(entry_yr),
                                    Gender=int(gen), is_primary=prim, is_secondary=sec, stage=stage,
                                    Age=date(int(dob[0]), int(dob[1]), int(dob[2])))
                d_student.user.is_student = True
                d_student.School = school
                d_student.save()
                message = 'Your Username is ' + username
                return render(request, 'home.html', {'message': message})
        else:
            error = 'Passwords must match'
            status = 'danger'
            return render(request, 'account/signup_student.html',
                          {'error': error, 'status': status, 'schools': School.objects.all(), 'classes': classes})
    else:
        pass
    return render(request, 'account/signup_student.html', {'schools': School.objects.all(), 'classes': classes})


def get_username(school, num, status, fn, ln):
    word_list = re.split(' ', school)
    abb = ''
    for word in word_list:
        abb += word[:1].lower()

    return str(fn.lower() + '.' + ln.lower() + '/' + abb + '/' + num + '/' + status.lower())


def get_class():
    list_ = []
    for i in range(1, 13):
        if 6 < i < 10:
            list_.append('JSS ' + str(i - 6))
        elif 0 < i < 7:
            list_.append('Primary ' + str(i))
        else:
            list_.append('SSS ' + str(i - 9))
    return list_
