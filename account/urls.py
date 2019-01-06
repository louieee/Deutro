from django.urls import path

from account.views import login, signup, signup_student, signup_teacher

urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('signup/student/', signup_student, name='student_signup'),
    path('signup/teacher/', signup_teacher, name='teacher_signup')
]
