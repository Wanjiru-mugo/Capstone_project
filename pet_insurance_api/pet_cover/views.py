from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import InsuranceCompany, VetClinic, Benefit, Plan, ExclusiveOf
from .serializers import InsuranceCompanySerializer, BenefitSerializer, VetClinicSerializer, ExclusiveOfSerializer, PlanSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class InsuranceCompanyViewSet(viewsets.ModelViewSet):
    queryset = InsuranceCompany.objects.all()
    serializer_class = InsuranceCompanySerializer
    permission_classes = [IsAdminOrReadOnly]

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['insurance_company']
    search_fields = ['insurance_company', 'vet_clinic']

class BenefitViewSet(viewsets.ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
    permission_classes = [IsAdminOrReadOnly]

class ExclusiveOfViewSet(viewsets.ModelViewSet):
    queryset = ExclusiveOf.objects.all()
    serializer_class = ExclusiveOfSerializer
    permission_classes = [IsAdminOrReadOnly]

class VetClinicViewSet(viewsets.ModelViewSet):
    queryset = VetClinic.objects.all()
    serializer_class = VetClinicSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['address', 'name']