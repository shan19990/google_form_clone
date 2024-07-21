from django.shortcuts import render ,redirect
from django.contrib import messages
import requests

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')