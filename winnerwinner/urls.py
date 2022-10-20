from django.urls import path
from .views import WinnerList, WinnerDetail

urlpatterns = [
    path("", WinnerList.as_view(), name="winner_list"),
    path("<int:pk>/", WinnerDetail.as_view(), name="winner_detail"),
]
