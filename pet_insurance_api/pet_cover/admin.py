from django.contrib import admin

#Register your models here.
from .models import InsuranceCompany, VetClinic, Plan, Benefit, ExclusiveOf

admin.site.register(InsuranceCompany)
admin.site.register(VetClinic)
admin.site.register(Plan)
admin.site.register(Benefit)
admin.site.register(ExclusiveOf)
