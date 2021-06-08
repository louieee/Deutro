from django_multitenant.fields import *
from django_multitenant.models import *


# Create your models here.

class SchoolManager(TenantManagerMixin, models.Manager):
    pass


class School(TenantModel):
    tenant_id = 'id'
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    website = models.URLField()
    email = models.EmailField()
    Image = models.ImageField(upload_to='images/', default=None)

    # class Meta(object):
    #     unique_together = ["id", "store"]

    objects = SchoolManager()
