from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Youth
from youth import serializers

class YouthViewSet(viewsets.ModelViewSet):
    """Manage youths"""
    serializer_class = serializers.YouthDetailSerializer
    queryset = Youth.objects.all()
    authentication_classes = [TokenAuthentication]
    premission_classes = [IsAuthenticated]

    #default serialiser class is Detail and for list youth Youth Serialiser is used

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.YouthSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializer.save()
