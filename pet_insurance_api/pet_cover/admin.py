from django.contrib import admin

#Register your models here.
from .models import InsuranceCompany, VetClinic, Plan, Benefit, ExclusiveOf

class PlanAdmin(admin.ModelAdmin):
    list_filter = ('insurance_company',)

class BenefitAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)

class ExclusiveOfAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)

class VetClinicAdmin(admin.ModelAdmin):
    list_filter = ('address',)
    search_fields = ('address', 'name',)

admin.site.register(InsuranceCompany)
admin.site.register(VetClinic, VetClinicAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(ExclusiveOf, ExclusiveOfAdmin)
