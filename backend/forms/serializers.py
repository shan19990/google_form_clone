from rest_framework import serializers
from .models import *

class FormSerializers(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class FormListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id','title']

class ResponseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Response
        fields = ['id', 'user', 'response_data']

class FormSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    responses = ResponseSerializer(many=True, read_only=True, source='response_set')

    class Meta:
        model = Form
        fields = ['id', 'title', 'created_by', 'created_at', 'expire_at', 'metadata', 'responses']
