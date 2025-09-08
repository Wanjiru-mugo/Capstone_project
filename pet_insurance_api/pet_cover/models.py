from django.db import models

# Create your models here.
class InsuranceCompany(models.Model):
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.description}\n contact us at {self.contact_email}\n"

class VetClinic(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_phone = models.TextField()
    
    def __str__(self):
        return f"{self.name}\n {self.address}\n {self.contact_phone}\n"

class Plan(models.Model):
    name = models.CharField(max_length=200)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    premium = models.IntegerField()
    deductible = models.IntegerField()
    annual_limit = models.IntegerField()
    waiting_period = models.IntegerField()
    copay = models.IntegerField()
    vet_clinic = models.ManyToManyField(VetClinic, related_name='plans')

class Benefit(models.Model):
    name = models.TextField()
    description = models.TextField()
    plans = models.ManyToManyField(Plan, related_name='plans')

    def __str__(self):
        return f"{self.name}:\n {self.description}"

class ExclusiveOf(models.Model):
    name = models.TextField()
    description = models.TextField()
    plans = models.ManyToManyField(Plan)

    def __str__(self):
        return f"{self.name}:\n {self.description}\n"
