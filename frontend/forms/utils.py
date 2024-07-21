from cryptography.fernet import Fernet
from django.conf import settings

def decrypt_text(encrypted_text):
    key = settings.ENCRYPTION_KEY
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()
    return decrypted_text
