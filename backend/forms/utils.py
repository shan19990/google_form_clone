# utils.py
from cryptography.fernet import Fernet
from django.conf import settings

cipher_suite = Fernet(settings.ENCRYPTION_KEY)

def encrypt_text(text):
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt_text(encrypted_text):
    return cipher_suite.decrypt(encrypted_text.encode()).decode()
