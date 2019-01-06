from django import forms
from django.core.validators import MaxValueValidator

from school.models import School

schools = School.objects.all()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()


class SignupTeacherForm(forms.Form):
    First_Name = forms.CharField(max_length=255)
    Last_Name = forms.CharField(max_length=255)
    Gender = forms.TypedChoiceField()
    subject = forms.TypedChoiceField()
    School = forms.TypedChoiceField()
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()


class SignupStudentForm(forms.Form):
    First_Name = forms.CharField(max_length=255)
    Last_Name = forms.CharField(max_length=255)
    Entry_year = forms.IntegerField(validators=[MaxValueValidator(4)])
    Gender = forms.TypedChoiceField()
    is_primary = forms.BooleanField()
    is_secondary = forms.BooleanField()
    stage = forms.IntegerField(validators=[MaxValueValidator(6)])
    DOB = forms.DateField()
    School = forms.TypedChoiceField()
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()
