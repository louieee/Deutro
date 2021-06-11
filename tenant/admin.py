from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Admin)

admin.site.register(Teacher)

admin.site.register(Student)

admin.site.register(Session)

admin.site.register(Class)

admin.site.register(Curriculum)

admin.site.register(CurriculumItem)

admin.site.register(Test)

admin.site.register(Question)

admin.site.register(QuestionOption)

admin.site.register(Result)

