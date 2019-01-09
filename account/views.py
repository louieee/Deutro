import re
from datetime import date

from django.shortcuts import render, redirect

from school.models import School
from student.models import Student
from student.models import User


# Create your views here.
def login(request):
    return render(request, 'account/login.html')


def signup(request):

    return render(request, 'account/signup.html')


def logout(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})


def signup_teacher(request):
    return render(request, 'account/signup_teacher.html')


def signup_student(request):
    if request.method == 'POST':
        fn = str(request.POST.get('firstname', False))
        ln = str(request.POST.get('lastname', False))
        age = str(request.POST.get('age', False))
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
        stage = str(request.POST.get('stage', False))
        pass1 = str(request.POST.get('password1', False))
        pass2 = str(request.POST.get('password2', False))
        sch_id = int(Student.objects.all().count())
        number = 2000 + int(Student.objects.all().count())
        username = get_username(school, str(number), 'Student')
        if pass1 == pass2:
            try:
                error = 'User already exists'
                status = 'danger'
                user = User.objects.get(username=username)
                return render(request, 'account/signup_student.html',
                              {'error': error, 'status': status, 'schools': School.objects.all()})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=pass1, is_student=True)
                school = School.objects.all().get(name=school)
                d_student = Student(School_id=sch_id, user=user, First_Name=fn, Last_Name=ln, Entry_year=int(entry_yr),
                                    Gender=gen, is_primary=prim, is_secondary=sec, stage=int(stage),
                                    Age=date(int(dob[0]), int(dob[1]), int(dob[2])))
                d_student.user.is_student = True
                d_student.School = school
                d_student.save()
                return redirect('home')
        else:
            error = 'Passwords must match'
            status = 'danger'
            return render(request, 'account/signup_student.html',
                          {'error': error, 'status': status, 'schools': School.objects.all()})
    else:
        pass
    return render(request, 'account/signup_student.html', {'schools': School.objects.all()})


def get_username(school, num, status):
    word_list = re.split(' ', school)
    abb = ' '
    for word in word_list:
        abb += word[:1]

    return abb + '/' + status + '/' + num
