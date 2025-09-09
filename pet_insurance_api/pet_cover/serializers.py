from rest_framework import serializers
from .models import InsuranceCompany, Benefit, Plan, ExclusiveOf, VetClinic

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ['id', 'name', 'description']

class ExclusiveOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExclusiveOf
        fields = ['id', 'name', 'description']

class VetClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetClinic
        fields = ['id', 'name', 'address', 'contact_phone']

class PlanSerializer(serializers.ModelSerializer):

    #return plan API with related benefits, exclusions, vetservice
    #benefits = BenefitSerializer(many=True, read_only=True)
    #exclusions = ExclusiveOfSerializer(many=True, read_only=True)
    #vetservice = VetClinicSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = ['id', 'name', 'insurance_company', 'premium', 'deductible', 'annual_limit', 'waiting_period', 'copay', 'vet_clinic']

    def validate(self, data):
        #premium value should be less that annual_limit
        premium = data.get('premium')
        annual_limit = data.get('annual_limit')

        if premium is not None and annual_limit is not None:
            if premium >= annual_limit:
                raise serializers.ValidationError(
                    {"premium": ['Premium value must be less than annual limit'],
                     'annual_limit': ['Annual limit must be greater than the premium value paid']
                     }
                )
            
class InsuranceCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceCompany
        fields = ['id', 'name', 'description', 'contact_email']