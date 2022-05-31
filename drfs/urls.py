from django.urls import path
from .views import DrfList, DrfDetail

urlpatterns = [
  path("",DrfList.as_view(), name="drf_list"),
  path("<int:pk>/", DrfDetail.as_view(), name="drf_detail")
]
