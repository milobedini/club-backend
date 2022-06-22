from django.shortcuts import render
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status

from squad.models import Squad
from squad.serializers.common import SquadSerializer

from .serializers.populated import PopulatedSquadSerializer

# Create your views here.


class SquadListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        squads = Squad.objects.all()
        serialized_squads = PopulatedSquadSerializer(squads, many=True)

        return Response(serialized_squads.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data["admin_members"] = [request.user.id]
        request.data["members"] = [request.user.id]
        squad_to_create = SquadSerializer(data=request.data)
        if squad_to_create.is_valid():
            squad_to_create.save()
            return Response(squad_to_create.data, status=status.HTTP_201_CREATED)
        return Response(squad_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class SearchSquads(APIView):
    def get(self, request, term):
        squads = Squad.objects.filter(name__icontains=term)
        serialized_squads = PopulatedSquadSerializer(squads, many=True)

        return Response(serialized_squads.data, status=status.HTTP_200_OK)


class SquadDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        squad = Squad.objects.get(pk=pk)
        serialized_squad = PopulatedSquadSerializer(squad)
        return Response(serialized_squad.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            squad_to_update = Squad.objects.get(pk=pk)
        except Squad.DoesNotExist:
            raise NotFound("Club not found.")
        # Remove user if already in squad.
        check_for_user = squad_to_update.members.filter(id=request.user.id)
        if len(check_for_user) != 0:
            # raise PermissionDenied("User already in squad")
            squad_to_update.members.remove(request.user)
            return Response(
                {"Success": f"{request.user.name} successfully removed from {squad_to_update.name}"},
                status=status.HTTP_200_OK,
            )
        #  Otherwise add user to squad.
        squad_to_update.members.add(request.user)
        return Response(
            {"Success": f"{request.user.name} successfully added to {squad_to_update.name}"}, status=status.HTTP_200_OK
        )


class AdminControlSquad(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, member):
        try:
            squad_to_update = Squad.objects.get(pk=pk)
        except Squad.DoesNotExist:
            raise NotFound("Club not found.")

        # check current user is admin for the club.
        check_admin = squad_to_update.admin_members.filter(id=request.user.id)
        if len(check_admin) == 0:
            raise PermissionDenied(f"User is not an admin member for {squad_to_update.name}")

        # Remove user if already in squad.
        check_for_user = squad_to_update.members.filter(id=member)
        if len(check_for_user) != 0:
            # raise PermissionDenied("User already in squad")
            squad_to_update.members.remove(member)
            return Response(
                {"Success": f"User successfully removed from {squad_to_update.name}"},
                status=status.HTTP_202_ACCEPTED,
            )
        #  Otherwise add user to squad.
        squad_to_update.members.add(member)
        return Response(
            {"Success": f"Successfully added to {squad_to_update.name}"},
            status=status.HTTP_202_ACCEPTED,
        )
