from os import stat

from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from squad.models import Squad

from events.serializers.common import EventSerializer

from .models import Event
from .serializers.populated import PopulatedEventSerializer

# Create your views here.


class EventListView(APIView):
    permission_classes = (IsAuthenticated,)

    # Need to ensure only club members can see/change/delete events.

    def get(self, request, pk):
        events = Event.objects.filter(club=pk)
        try:
            club = Squad.objects.get(pk=pk)
        except Squad.DoesNotExist:
            raise NotFound(detail="Club does not exist.")
        check_if_club_member = club.members.filter(id=request.user.id)
        if len(check_if_club_member) == 0:
            raise PermissionDenied(detail="User is not in this club.")
        serialized_events = PopulatedEventSerializer(events, many=True)
        return Response(serialized_events.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        request.data["club"] = pk
        request.data["participants"] = [request.user.id]
        club = Squad.objects.get(pk=pk)
        check_if_club_member = club.members.filter(id=request.user.id)
        if len(check_if_club_member) == 0:
            raise PermissionDenied(detail="User is not in this club.")
        event_to_create = EventSerializer(data=request.data)
        if event_to_create.is_valid():
            event_to_create.save()
            return Response(event_to_create.data, status=status.HTTP_201_CREATED)
        return Response(event_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class EventDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, id):
        event = Event.objects.get(pk=id)
        serialized_event = PopulatedEventSerializer(event)
        return Response(serialized_event.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, id):
        try:
            event_to_delete = Event.objects.get(pk=id)
        except Event.DoesNotExist:
            raise NotFound(detail="Event not found.")

        squad = Squad.objects.get(pk=pk)
        check_if_club_admin = squad.admin_members.filter(id=request.user.id)
        if len(check_if_club_admin) == 0:
            raise PermissionDenied(detail="User is not an admin member of this club.")

        event_to_delete.delete()
        return Response({"Successfully deleted event."}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, id):
        try:
            event_to_update = Event.objects.get(pk=id)
        except Event.DoesNotExist:
            raise NotFound("Event not found.")

        # Check if user is in the club.
        club = Squad.objects.get(pk=pk)
        check_if_club_member = club.members.filter(id=request.user.id)
        if len(check_if_club_member) == 0:
            raise PermissionDenied(detail="User is not in this club.")

        # Remove user if already attending.
        check_for_user = event_to_update.participants.filter(id=request.user.id)
        if len(check_for_user) != 0:
            event_to_update.participants.remove(request.user)
            return Response(
                {"Success": f"User successfully removed from event."},
                status=status.HTTP_202_ACCEPTED,
            )

        # Otherwise add user to participants list.
        event_to_update.participants.add(request.user)
        return Response(
            {"Success": f"{request.user.name} successfully added to participants list."},
            status=status.HTTP_202_ACCEPTED,
        )
