from rest_framework import generics
from .models import Sound
from .permissions import IsOwnerOrReadOnly
from .serializers import SoundSerializer
# Create your views here.

class SoundList(generics.ListCreateAPIView):
  queryset = Sound.objects.all()
  serializer_class = SoundSerializer
  
class SoundDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Sound.objects.all()
  serializer_class = SoundSerializer
  permission_classes = (IsOwnerOrReadOnly),