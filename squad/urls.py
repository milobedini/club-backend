from django.urls import path

from . import views

urlpatterns = [path("", views.SquadListView.as_view())]
