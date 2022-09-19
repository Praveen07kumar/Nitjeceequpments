import os
import json
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'equipments/home.html')

def communicationLab(request):
    return render(request, 'equipments/communicationLab.html',{"img":"/static/images/lab1.jpg"})

def microwaveLab(request):
    return render(request, 'equipments/microwaveLab.html',{"img":"/static/images/lab1.jpg"})

def devicesLab(request):
    return render(request, 'equipments/devicesLab.html',{"img":"/static/images/lab1.jpg"})

def vlsiLab(request):
    return render(request, 'equipments/vlsiLab.html',{"img":"/static/images/lab1.jpg"})

def bioMedicalLab(request):
    return render(request, 'equipments/bioMedicalLab.html',{"img":"/static/images/lab1.jpg"})

def medicalImagingLab(request):
    return render(request, 'equipments/medicalImagingLab.html',{"img":"/static/images/lab1.jpg"})

def embeddedLab(request):
    return render(request, 'equipments/embeddedLab.html',{"img":"/static/images/lab1.jpg"})

def emergingLab(request):
    return render(request, 'equipments/emergingLab.html',{"img":"/static/images/lab1.jpg"})

def BECLab(request):
    return render(request, 'equipments/BECLab.html',{"img":"/static/images/lab1.jpg"})

def DSPLab(request):
    return render(request, 'equipments/DSPLab.html',{"img":"/static/images/lab1.jpg"})
