from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Domain


class DomainAdmin(admin.ModelAdmin):
    fields = ('domain', 'name')
    ordering = ('domain',)


admin.site.register(Domain, DomainAdmin)
