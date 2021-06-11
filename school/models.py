from django.db import models
from tenant_schemas.models import TenantMixin


# Create your models here.


class School(TenantMixin):
    name = models.CharField(max_length=50, default='', unique=True)
    contact_info = models.ManyToManyField('users.Contact')
    domains = models.ManyToManyField('domain.Domain')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    auto_create_schema = True

    def __str__(self):
        return self.name
