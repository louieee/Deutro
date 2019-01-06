from django.shortcuts import render


def give_assignment(request):
    return render(request, 'teacher/give_assignment.html')


def upload_result(request):
    return render(request, 'teacher/upload_result.html')


def view_assignments(request):
    return render(request, 'teacher/view_assignments.html')


def dashboard(request):
    return render(request, 'teacher/dashboard.html')
