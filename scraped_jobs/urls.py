from django.urls import path
from .views import ActiveJobList, ActiveJobDetail

urlpatterns = [
    path("", ActiveJobList.as_view(), name="active_job_list"),
    path("<int:pk>/", ActiveJobDetail.as_view(), name="active_job_detail"),
]
