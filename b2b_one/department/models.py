from django.contrib.auth.models import Permission
from django.db import models

from tenant.models import Tenant

# Create your models here.

class Department(models.Model):
    company = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100, unique=False)

    class Meta:
        unique_together = ('company', 'department_name')

    def __str__(self):
        return self.company.company + ' - ' + self.department_name