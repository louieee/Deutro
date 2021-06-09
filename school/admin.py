from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(School)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Curriculum)
admin.site.register(CurriculumItem)
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(Question)
admin.site.register(QuestionOption)