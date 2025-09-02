from rest_framework import serializers
from .models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'established', 'type']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'date_hired', 'company']