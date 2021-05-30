from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=150, null=True)
    age = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=200)
    edited_on = models.DateTimeField(auto_now=True, null=True)
    edited_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "bmc_emp"

    def __str__(self):
        return self.name