from django.urls import path
from .views import SoundList, SoundDetail

urlpatterns = [
  path("",SoundList.as_view(), name="sound_list"),
  path("<int:pk>/", SoundDetail.as_view(), name="sound_detail"),
]
