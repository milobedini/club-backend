from django.shortcuts import render
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
