from django.urls import path

from . import views

urlpatterns = [
    path("", views.SquadListView.as_view()),
    path("search/<str:term>/", views.SearchSquads.as_view()),
    path("<int:pk>/", views.SquadDetailView.as_view()),
    path("<int:pk>/<int:member>/", views.AdminControlSquad.as_view()),
    path("<int:pk>/<int:member>/admin/", views.UpdateAdmin.as_view()),
    path("<int:pk>/request/", views.RequestToAdmin.as_view()),
    path("<int:pk>/request/<int:applicant>/accept", views.AdminAccept.as_view()),
    path("<int:pk>/request/<int:applicant>/reject", views.AdminReject.as_view()),
]
