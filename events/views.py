from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event
from .serializers.populated import PopulatedEventSerializer

# Create your views here.


class EventListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        events = Event.objects.filter(club=pk)
        serialized_events = PopulatedEventSerializer(events, many=True)
        return Response(serialized_events.data, status=status.HTTP_200_OK)
