from django.db import models
from django.contrib.auth.models import User

class Form(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    expire_at = models.DateField()
    metadata = models.JSONField()  # To store questions and options as JSON

    def __str__(self):
        return self.title

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    response_data = models.JSONField()  # To store answers as JSON

    def __str__(self):
        return f'Response for {self.form.title}'
