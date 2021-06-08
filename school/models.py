from django.db import models


# Create your models here.

class Choice:
    class Term:
        first, second, third, fourth, fifth = range(5)

    term = (
        (Term.first, 'First'), (Term.second, 'Second'), (Term.third, 'Third'),
        (Term.fourth, 'Fourth'), (Term.fifth, 'Fifth')
    )

    class Difficulty:
        easy, medium, hard, very_hard, advanced = range(5)

    difficulty = (
        (Difficulty.easy, 'Easy'), (Difficulty.medium, 'Medium'), (Difficulty.hard, 'Hard'),
        (Difficulty.very_hard, 'Very Hard'), (Difficulty.advanced, 'Advanced')
    )

    class Option:
        objective, subjective, theory = range(3)

    option = (
        (Option.objective, 'Objective'), (Option.subjective, 'Subjective'), (Option.theory, 'Theory')
    )

    class Test:
        class_work, home_work, class_test, exam = range(4)

    test_type = (
        (Test.class_work, 'Class Work'), (Test.home_work, 'Home Work'),
        (Test.class_test, 'Class Test'), (Test.exam, 'Exam')
    )


class School(models.Model):
    name = models.CharField(max_length=50, default='')
    contact_info = models.ManyToManyField('users.Contact')
    domains = models.ManyToManyField('domain.Domain')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Teacher(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('school.Subject')
    classes = models.ManyToManyField('school.Class')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subject(models.Model):
    name = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Class(models.Model):
    institution = models.CharField(max_length=30, default='')
    level = models.CharField(max_length=20, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='user')
    school = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='school')
    class_s = models.ForeignKey('school.Class', on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField('school.Subject')
    guardians = models.ManyToManyField('users.User', limit_choices_to={'is_parent': True}, related_name='guardians')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Curriculum(models.Model):
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    class_s = models.ForeignKey('school.Class', on_delete=models.CASCADE)
    subject = models.ForeignKey('school.Subject', on_delete=models.CASCADE)
    term = models.PositiveSmallIntegerField(choices=Choice.term, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CurriculumItem(models.Model):
    curriculum = models.ForeignKey('school.Curriculum', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    difficulty = models.PositiveSmallIntegerField(choices=Choice.difficulty, null=True, default=None)
    start_date = models.DateTimeField(blank=True, default=None, null=True)
    end_date = models.DateTimeField(blank=True, default=None, null=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Test(models.Model):
    type = models.PositiveSmallIntegerField(choices=Choice.test_type, null=True, default=None)
    curriculum = models.ForeignKey('school.Curriculum', on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, default=None, null=True)
    end_date = models.DateTimeField(blank=True, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Result(models.Model):
    test = models.ForeignKey('school.Test', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey('school.Student', on_delete=models.CASCADE)
    score = models.DecimalField(decimal_places=2, max_digits=6)
    report = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    test = models.ForeignKey('school.Test', on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=Choice.option, null=True, default=None)
    question = models.TextField()
    score = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QuestionOption(models.Model):
    question = models.ForeignKey('school.Question', on_delete=models.CASCADE)
    content = models.TextField()
    answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)