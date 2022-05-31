from rest_framework import generics
from .models import Drf
from .serializers import DrfSerializer
# Create your views here.

class DrfList(generics.ListCreateAPIView):
  queryset = Drf.objects.all()
  serializer_class = DrfSerializer
  
class DrfDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Drf.objects.all()
  serializer_class = DrfSerializer