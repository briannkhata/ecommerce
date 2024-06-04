from rest_framework import serializers
from .models import Payment_Type

class Payment_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Type
        fields = '__all__'
        # fields = ['Plan_id','plan_name']

