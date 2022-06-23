from django.urls import path

from .views import EventDetailView, EventListView

urlpatterns = [
    path("<int:pk>/", EventListView.as_view()),
    path("<int:pk>/<int:id>/", EventDetailView.as_view()),
]
