from django.shortcuts import render, get_object_or_404

from assignment.models import Assignment


def assignments(request):
    return render(request, 'student/assignments.html')


def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    return render(request, 'student/assignment_detail.html', {'assignment': assignment})


def check_result(request):
    return render(request, 'student/check_result.html')


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'student/dashboard.html')
