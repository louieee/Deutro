from django.shortcuts import render, get_object_or_404

from .models import School


# Create your views here.

def add_school(request):
    return render(request, 'school/add_school.html')


def view_schools(request):
    return render(request, 'school/school_list.html')


def school_detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    return render(request, 'school/school_detail.html', {'school': school})
