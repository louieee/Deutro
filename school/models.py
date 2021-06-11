from django_multitenant.fields import *
from django_multitenant.models import *


# Create your models here.

class SubjectManager(TenantManager):
    def show_all(self):
        return self.all()


class Subject(TenantModel):
    name = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SubjectManager()

    def __init__(self):
        super().__init__(self)


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


class School(TenantModel):
    tenant_id = 'id'
    name = models.CharField(max_length=50, default='')
    contact_info = models.ManyToManyField('users.Contact')
    domains = models.ManyToManyField('domain.Domain')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self):
        super().__init__(self)


class TeacherManager(TenantManager):
    def show_all(self):
        return self.all()


class Teacher(TenantModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    tenant_id = 'school_id'
    subjects = models.ManyToManyField('school.Subject')
    classes = models.ManyToManyField('school.Class')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TeacherManager()

    def __init__(self):
        super().__init__(self)


class AdminManager(TenantManager):
    def show_all(self):
        return self.all()


class Admin(TenantModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    tenant_id = 'school_id'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AdminManager()

    def __init__(self):
        super().__init__(self)


class ClassManager(TenantManager):
    def show_all(self):
        return self.all()


class Class(TenantModel):
    institution = models.PositiveSmallIntegerField(choices=Choice.institution, default=Choice.Institution.pre_school)
    level = models.CharField(max_length=20, default='')
    school = models.ForeignKey('school.School', on_delete=models.CASCADE, null=True)
    tenant_id = 'school_id'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ClassManager()

    def __init__(self):
        super().__init__(self)

    class Meta:
        verbose_name_plural = 'Classes'


class StudentManager(TenantManager):
    def show_all(self):
        return self.all()


class Student(TenantModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    guardians = models.ManyToManyField('users.User', limit_choices_to={'is_parent': True}, related_name='guardians')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SubjectManager()

    def __init__(self):
        super().__init__(self)


class SessionManager(TenantManager):
    def show_all(self):
        return self.all()


class Session(TenantModel):
    student = TenantForeignKey('school.Student', on_delete=models.CASCADE)
    term = models.PositiveSmallIntegerField(choices=Choice.term, null=True, default=None)
    entry_year = models.DateField()
    class_level = TenantForeignKey('school.Class', on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField('school.Subject')
    report = models.JSONField()

    objects = SessionManager()

    def __init__(self):
        super().__init__(self)


class CurriculumManager(TenantManager):
    def show_all(self):
        return self.all()


class Curriculum(TenantModel):
    subject = TenantForeignKey('school.Subject', on_delete=models.CASCADE)
    class_level = TenantForeignKey('school.Class', on_delete=models.CASCADE)
    term = models.PositiveSmallIntegerField(choices=Choice.term, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CurriculumManager()

    def __init__(self):
        super().__init__(self)


class CurriculumItemManager(TenantManager):
    def show_all(self):
        return self.all()


class CurriculumItem(TenantModel):
    curriculum = TenantForeignKey('school.Curriculum', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    difficulty = models.PositiveSmallIntegerField(choices=Choice.difficulty, null=True, default=None)
    start_date = models.DateTimeField(blank=True, default=None, null=True)
    end_date = models.DateTimeField(blank=True, default=None, null=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CurriculumItemManager()

    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return self.title


class TestManager(TenantManager):
    def show_all(self):
        return self.all()


class Test(TenantModel):
    type = models.PositiveSmallIntegerField(choices=Choice.test_type, null=True, default=None)
    curriculum = TenantForeignKey('school.Curriculum', on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, default=None, null=True)
    end_date = models.DateTimeField(blank=True, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TestManager()

    def __init__(self):
        super().__init__(self)


class Result(TenantModel):
    test = TenantForeignKey('school.Test', on_delete=models.SET_NULL, null=True)
    session = TenantForeignKey('school.Session', on_delete=models.CASCADE, null=True)
    score = models.DecimalField(decimal_places=2, max_digits=6)
    report = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self):
        super().__init__(self)


class Question(TenantModel):
    test = TenantForeignKey('school.Test', on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(choices=Choice.option, null=True, default=None)
    question = models.TextField()
    score = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self):
        super().__init__(self)


class QuestionOption(TenantModel):
    question = TenantForeignKey('school.Question', on_delete=models.CASCADE)
    content = models.TextField()
    answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self):
        super().__init__(self)
