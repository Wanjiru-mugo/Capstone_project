from django.db import models

# Create your models here.
<<<<<<< HEAD
=======
class InsuranceCompany(models.Model):
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    description = models.TextField()

class Plan(models.Model):
    name = models.CharField(max_length=200)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    premium = models.DecimalField()
    deductible = models.DecimalField()
    annual_limit = models.DecimalField()
    waiting_period = models.IntegerField()
    copay = models.DecimalField()
    vet_clinic = models.ManyToManyField(VetClinic, related_name='plans')
    
class Benefit(models.Model):
    name = models.TextField()
    description = models.TextField()
    plans = models.ManyToManyField(Plan, related_name='plans')

class ExclusiveOf(models.Model):
    name = models.TextField()
    description = models.TextField()
    plans = models.ManyToManyField(Plan)

class VetClinic(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_phone = models.TextField()
    services = models.TextField()

>>>>>>> feat/databaseModels
