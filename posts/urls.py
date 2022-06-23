from django.urls import path

from .views import PostDetailView, PostsListView

urlpatterns = [
    path("<int:pk>/", PostsListView.as_view()),
    path("<int:pk>/<int:id>/", PostDetailView.as_view()),
]
