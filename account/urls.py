from django.urls import path

from account.views import LoginView, signup, signup_student, signup_teacher

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('signup', signup, name='signup'),
    path('signup/student/', signup_student, name='student_signup'),
    path('signup/teacher/', signup_teacher, name='teacher_signup')
]
