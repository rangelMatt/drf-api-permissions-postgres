from rest_framework import serializers
from .models import Drf

class DrfSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'name', 'description', 'created_at')
    model = Drf
    
    