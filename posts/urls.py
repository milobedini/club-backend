from django.urls import path

from .views import PostsListView

urlpatterns = [
    path("<int:pk>/", PostsListView.as_view()),
]
