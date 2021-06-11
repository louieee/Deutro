from django.db import models


# Create your models here.




class Choice:
    class Term:
        first, second, third, fourth, fifth = range(5)

    class Institution:
        pre_school, high_school, university = range(3)

    institution = (
        (Institution.pre_school, 'Pre School'), (Institution.high_school, 'High School'),
        (Institution.university, 'University')
    )

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


class Teacher(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('shared.Subject')
    classes = models.ManyToManyField('Class')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Admin(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.school}: {self.title}'


class Class(models.Model):
    institution = models.PositiveSmallIntegerField(choices=Choice.institution, default=Choice.Institution.pre_school)
    level = models.CharField(max_length=20, default='')
    school = models.ForeignKey('school.School', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.school}: {self.level}'

    class Meta:
        verbose_name_plural = 'Classes'


class Student(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    guardians = models.ManyToManyField('users.User', limit_choices_to={'is_parent': True}, related_name='guardians')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Session(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    term = models.PositiveSmallIntegerField(choices=Choice.term, null=True, default=None)
    entry_year = models.DateField()
    class_level = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField('shared.Subject')
    report = models.JSONField()

    def __str__(self):
        return f'{self.get_term_display()} term for {self.entry_year.year} for {self.student}'


class Curriculum(models.Model):
    subject = models.ForeignKey('shared.Subject', on_delete=models.CASCADE)
    class_level = models.ForeignKey('Class', on_delete=models.CASCADE)
    term = models.PositiveSmallIntegerField(choices=Choice.term, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject} for {self.class_level} for {dict(Choice.term)[self.term]} term.'


class CurriculumItem(models.Model):
    curriculum = models.ForeignKey('Curriculum', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    difficulty = models.PositiveSmallIntegerField(choices=Choice.difficulty, null=True, default=None)
    start_date = models.DateTimeField(blank=True, default=None, null=True)
    end_date = models.DateTimeField(blank=True, default=None, null=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    type = models.PositiveSmallIntegerField(choices=Choice.test_type, null=True, default=None)
    curriculum = models.ForeignKey('Curriculum', on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, default=None, null=True)
    end_date = models.DateTimeField(blank=True, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Test for {self.curriculum}'


class Result(models.Model):
    test = models.ForeignKey('Test', on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE, null=True)
    score = models.DecimalField(decimal_places=2, max_digits=6)
    report = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.session.student} Result test for {self.test}'


class Question(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=Choice.option, null=True, default=None)
    question = models.TextField()
    score = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class QuestionOption(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    content = models.TextField()
    answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
