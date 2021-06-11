from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


# Create your models here.


class School(TenantMixin):
    name = models.CharField(max_length=50, default='', unique=True)
    contact_info = models.ManyToManyField('shared.Contact')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
