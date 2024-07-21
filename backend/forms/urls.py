# mainapp/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path('create/', FormCreateView.as_view(), name="create"),
    path('list/', FormsListView.as_view(), name="list"),
    path('fetch/<int:id>/', FormDetailView.as_view(), name="fetch"),

    path('response/create/', ResponseCreateView.as_view(), name="response_create"),
    path('response/fetch/<int:id>/', ResponseListView.as_view(), name="response_fetch"),

    path('user/list/', UserFormsView.as_view(), name='user_forms'),

    path('form/<int:form_id>/export/', export_excel, name='export_responses_to_excel'),
    path('form/send_mail/', send_mail, name='send_mail'),
]
