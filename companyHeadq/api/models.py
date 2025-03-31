from django.db import models

# Create your models here.
# company models
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(
        ('IT', 'IT Company'),
        ('Finance', 'Finance Company'),
        ('Healthcare', 'Healthcare Company'),
        ('Education', 'Education Institute'),
        ('Other', 'Other')
        ))
    active = models.BooleanField(default=True)
