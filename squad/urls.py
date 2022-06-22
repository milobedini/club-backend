from django.urls import path

from . import views

urlpatterns = [
    path("", views.SquadListView.as_view()),
    path("search/<str:term>/", views.SearchSquads.as_view()),
    path("<int:pk>/", views.SquadDetailView.as_view()),
    path("<int:pk>/<int:member>/", views.AdminControlSquad.as_view()),
]
