from rest_framework import serializers
from .models import *

class StringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringData
        fields = "__all__"