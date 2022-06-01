from rest_framework import serializers
from .models import Sound

class SoundSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'name', 'description', 'created_at')
    model = Sound
    
    