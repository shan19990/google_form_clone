from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .utils import *

# Create your views here.

def create_form(request):
    return render(request,"forms/create_form.html")

def list_form(request):
    return render(request,"forms/show_form.html")

def edit_form(request):
    return render(request,"forms/edit_form.html")

def response(request):
    return render(request,"forms/show_responses.html")

def fill_form(request, encrypted_id):
    try:
        decrypted_id = decrypt_text(encrypted_id)
        print(decrypted_id)
        return render(request, "forms/fill_form.html", {
            "decrypted_id": decrypted_id,
            "encrypted_id": encrypted_id,
            "encryption_key": settings.ENCRYPTION_KEY.decode('utf-8')  # Ensure the key is a string
        })
    except Exception as e:
        return render(request, "forms/error.html", {"error": str(e)})



def send_form(request):
    return render(request,"forms/send_form.html")

def thank_you(request):
    return render(request, "forms/thank_you.html")

def dashboard(request):
    return render(request, "forms/dashboard_form.html")