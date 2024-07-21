from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import pandas as pd
import json
from django.http import JsonResponse
from django.core.mail import send_mail as django_send_mail
from rest_framework.decorators import api_view, permission_classes
from .utils import encrypt_text, decrypt_text
from django.conf import settings

# Create your views here.

class FormCreateView(generics.CreateAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class FormsListView(generics.ListAPIView):
    serializer_class = FormListSerializers
    queryset = Form.objects.all()


class FormListView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = FormSerializers
    queryset = Form.objects.all()


class ResponseCreateView(generics.CreateAPIView):
    serializer_class = ResponseSerializers
    queryset = Response.objects.all()


class ResponseListView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ResponseSerializers
    queryset = Response.objects.all()


class FormDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    lookup_field = 'id'


def export_excel(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    responses = Response.objects.filter(form=form)

    # Initialize the data list with headers
    headers = ['Response ID'] + [question['text'] for question in form.metadata['questions']]
    data = [headers]

    # Add responses for each user
    for response in responses:
        row = [response.id]  # Start with the response ID
        
        for index, question in enumerate(form.metadata['questions']):
            question_id = f'q{index + 1}'
            question_text = question['text']
            answer = response.response_data.get(question_id, '')
            row.append(answer)
        
        data.append(row)

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data[1:], columns=data[0])

    # Create an HTTP response with the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{form.title}.xlsx"'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Responses')

    return response




class UserFormsView(generics.ListAPIView):
    serializer_class = FormSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Form.objects.filter(created_by=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_mail(request):
    if request.method == 'POST':
        data = request.data
        form_id = data.get('form_id')
        emails = data.get('emails', [])

        form = get_object_or_404(Form, id=form_id)
        encrypted_form_id = encrypt_text(str(form_id))
        encryption_key = settings.ENCRYPTION_KEY.decode()
        form_url = f"http://127.0.0.1:8000/fill/{encrypted_form_id}/"

        for email in emails:
            django_send_mail(
                subject=f"Please fill out the form: {form.title}",
                message=f"Click the following link to fill out the form: {form_url}",
                from_email='your-email@example.com',
                recipient_list=[email]
            )

        return JsonResponse({'message': 'Form sent successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
