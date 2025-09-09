"""
URL configuration for pet_insurance_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pet_cover.views import InsuranceCompanyViewSet, BenefitViewSet, PlanViewSet, VetClinicViewSet, ExclusiveOfViewSet
from rest_framework.routers import DefaultRouter
from pet_cover.models import InsuranceCompany, Benefit, VetClinic, Plan, ExclusiveOf
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'insurance_companies', InsuranceCompanyViewSet, basename='insurance_company')
router.register(r'benefits', BenefitViewSet, basename='benefit')
router.register(r'plans', PlanViewSet, basename='plan')
router.register(r'vet_clinics', VetClinicViewSet, basename='vet_clinic')
router.register(r'exclusive_of', ExclusiveOfViewSet, basename='exclusive_of')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
