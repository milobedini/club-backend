from django.urls import path

from .views import LoginView, ProfileListView, ProfileView, RegisterView, SearchUsers

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("profiles/", ProfileListView.as_view()),
    path("profiles/search/<str:term>/", SearchUsers.as_view()),
]
