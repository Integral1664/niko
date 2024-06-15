from django.shortcuts import render
from .models import Builders

def list(request):
    return render(request,'main/list.html')

def projectnew(request):
    return render(request,'main/projectnew.html')
