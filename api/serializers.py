from rest_framework import serializers
from .models import UrineStripImage

class UrineStripImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrineStripImage
        fields = ('image',)
