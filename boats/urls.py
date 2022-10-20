from django.urls import path
from .views import BoatList, BoatDetail

urlpatterns = [
    path("", BoatList.as_view(), name="job_list"),
    path("<int:pk>/", BoatDetail.as_view(), name="job_detail"),
]
