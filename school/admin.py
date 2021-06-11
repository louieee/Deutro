from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from school.models import School


@admin.register(School)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name',)
