from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import blogcontentlist

class blogSerializer (serializers.ModelSerializer):
    class Meta :
        model = blogcontentlist
        fields = '__all__'