from rest_framework import serializers
from core.models import User, Youth

class YouthSerializer(serializers.ModelSerializer):
    """Youth Serialisers"""
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model= Youth
        fields = ['email','first_name', 'last_name', 'birth_date', 'from_city_germany', 'from_city_india', 'phone_number', 'sabha_type' ]
        read_only_fields = ['id']

# Detail serialiser inherits the youth serialiser
class YouthDetailSerializer(YouthSerializer):
    """Youth Detail Seriealiser"""
    class Meta(YouthSerializer.Meta):
        fields = YouthSerializer.Meta.fields 
