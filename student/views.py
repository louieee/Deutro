from django.shortcuts import render, get_object_or_404

from Utilities.custom_views import DefaultView
from student.models import User
from assignment.models import Assignment
from .models import Student
from card.models import Card
from result.models import Result


def assignments(request):
    all_assignments = Assignment.objects.all()
    return render(request, 'student/assignments.html', {'assignments': all_assignments})


def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    return render(request, 'student/assignment_detail.html', {'assignment': assignment})


def check_result(request):
    if request == 'POST':
        username = str(request.POST.get('username', False))
        yr = str(request.POST.get('Year', False))
        term = str(request.POST.get('stage', False))
        pin = str(request.POST.get('code', False))
        try:
            user = User.objects.get(username=username)
            student = Student.objects.get(user=user.id)
            card_ = Card.objects.get(code=pin)
            result = Result.objects.get(student=student.id, Year=int(yr))
            if user and student and card_ and result:
                if card_.year == 0 and card_.term == 0 and card_.student_id == 0:
                    card_.year = int(yr)
                    card_.term = int(term[:1])
                    card_.student_id = int(student.id)
                    card_.save()
                    if term[:1] == '1':
                        return render(request, 'student/dashboard.html', {'result': result.First_term.url})
                    elif term[:1] == '2':
                        return render(request, 'student/dashboard.html', {'result': result.Second_term_term.url})
                    elif term[:1] == '3':
                        return render(request, 'student/dashboard.html', {'result': result.Third_term.url})
                elif card_.year == int(yr) and card_.student_id == int(student.id) and card_.term == int(term[:1]):
                    if term[:1] == '1':
                        return render(request, 'student/dashboard.html', {'result': result.First_term.url})
                    elif term[:1] == '2':
                        return render(request, 'student/dashboard.html', {'result': result.Second_term_term.url})
                    elif term[:1] == '3':
                        return render(request, 'student/dashboard.html', {'result': result.Third_term.url})
                else:
                    error = 'This card has already been used for another term'
                    return render(request, 'student/check_result.html', {'error': error})

        except User.DoesNotExist and Card.DoesNotExist and Result.DoesNotExist:
            error = 'Either Username or Pin is Incorrect'
            return render(request, 'student/check_result.html', {'error': error})

    return render(request, 'student/check_result.html')


class HomeView(DefaultView):
    context = {}
    template = 'home.html'


class DashboardView(DefaultView):
    template = 'student/dashboard.html'


class AboutView(DefaultView):
    template = 'about.html'
