from django.urls import path

from student.views import assignment_detail
from teacher.views import give_assignment, upload_result, dashboard

urlpatterns = [
    path('give_assignment/', give_assignment, name='give_assignment'),
    path('assignment/<int:assignment_id>/', assignment_detail, name='assignment_detail'),
    path('upload_result/', upload_result, name='upload_result'),
    path('dashboard/', dashboard, name='teacher_dashboard')
]
