from django.db import models

# Create your models here.
class InsuranceCompany(models.Model):
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    description = models.TextField()

class VetClinic(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_phone = models.TextField()
    services = models.TextField()

class Plan(models.Model):
    name = models.CharField(max_length=200)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    premium = models.DecimalField(max_digits=5, decimal_places=2)
    deductible = models.DecimalField(max_digits=5, decimal_places=2)
    annual_limit = models.DecimalField(max_digits=5, decimal_places=2)
    waiting_period = models.IntegerField()
    copay = models.DecimalField(max_digits=5, decimal_places=2)
    vet_clinic = models.ManyToManyField(VetClinic, related_name='plans')

class Benefit(models.Model):
    name = models.TextField()
    description = models.TextField()
    plans = models.ManyToManyField(Plan, related_name='plans')

class ExclusiveOf(models.Model):
    name = models.TextField()
    description = models.TextField()
    plans = models.ManyToManyField(Plan)
