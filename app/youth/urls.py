from django.urls import path, include
from rest_framework.routers import DefaultRouter
from youth import views

router = DefaultRouter()

router.register('youths', views.YouthViewSet)
app_name = 'youth'

urlpatterns = [
    path('',include(router.urls))
]