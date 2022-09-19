from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('communicationLab', views.communicationLab, name='communicationLab'),
    path('microwaveLab', views.microwaveLab, name='microwaveLab'),
    path('devicesLab', views.devicesLab, name='devicesLab'),
    path('vlsiLab', views.vlsiLab, name='vlsiLab'),
    path('bioMedicalLab', views.bioMedicalLab, name='bioMedicalLab'),
    path('medicalImagingLab', views.medicalImagingLab, name='medicalImagingLab'),
    path('embeddedLab', views.embeddedLab, name='embeddedLab'),
    path('emergingLab', views.emergingLab, name='emergingLab'),
    path('BECLab', views.BECLab, name='BECLab'),
    path('DSPLab', views.DSPLab, name='DSPLab'),
]
