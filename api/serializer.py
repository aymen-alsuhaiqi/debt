from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = '__all__'

class UpdateDeptSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    status = serializers.CharField(default="+/-")