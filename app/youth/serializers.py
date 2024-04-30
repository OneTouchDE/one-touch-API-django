from rest_framework import serializers
from core.models import Youth

class YouthSerializer(serializers.ModelSerializer):
    class Meta:
        model= Youth
        fields = ['email','first_name', 'last_name', 'birth_date', 'from_city_germany', 'from_city_india', 'phone_number', 'sabha_type' ]
        read_only_fields = ['id']

class YouthDetailSerializer(serializers.ModelSerializer):
    class Meta(YouthSerializer.Meta):
        fields = YouthSerializer.Meta.fields
