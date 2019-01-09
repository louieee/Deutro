from django.shortcuts import render, get_object_or_404

from assignment.models import Assignment
from .models import Student


def assignments(request):
    return render(request, 'student/assignments.html')


def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    return render(request, 'student/assignment_detail.html', {'assignment': assignment})


def check_result(request):
    return render(request, 'student/check_result.html')


def home(request):
    return render(request, 'home.html', {'users': Student.objects.all()})


def dashboard(request):
    student = Student.objects.all().get(pk=1)
    return render(request, 'student/dashboard.html', {'student': student})


def about(request):
    return render(request, 'about.html')
