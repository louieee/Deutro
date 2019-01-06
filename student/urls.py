from django.urls import path

from student.views import assignment_detail, assignments, check_result, dashboard

urlpatterns = [
    path('assignments/', assignments, name='all_assignments'),
    path('assignment/<int:assignment_id>/', assignment_detail, name='assignment_detail'),
    path('check_result/', check_result, name='result_checker'),
    path('dashboard/', dashboard, name='student_dashboard')
]
