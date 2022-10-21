from django.urls import path
from .views import JobList, JobDetail, NoteList, NoteDetail

urlpatterns = [
    path("", JobList.as_view(), name="job_list"),
    path("note/", NoteList.as_view(), name="note_list"),
    path("<int:pk>/", JobDetail.as_view(), name="job_detail"),
    path("note/<int:pk>/", NoteDetail.as_view(), name="note_detail"),
]
