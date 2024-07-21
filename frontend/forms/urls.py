from django.urls import path
from .views import *

urlpatterns = [
    # Other endpoints...
    path('create/', create_form, name='create'),
    path('edit/', edit_form, name='edit'),
    path('', list_form, name='list'),
    path('responses/', response, name='response'),
    path('send/', send_form, name='send_form'),
    path('fill/<str:encrypted_id>/', fill_form, name='fill_form'),
    path('dashboard/', dashboard, name='dashboard'),
    path('thankyou/', thank_you, name='thank_you'),
]
