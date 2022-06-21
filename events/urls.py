from django.urls import path

from .views import EventListView

urlpatterns = [
    path("<int:pk>/", EventListView.as_view()),
]
