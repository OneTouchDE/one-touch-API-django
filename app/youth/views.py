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

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.YouthSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
