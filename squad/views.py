from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from squad.models import Squad

from .serializers import SquadSerializer

# Create your views here.


class SquadListView(APIView):
    def get(self, request):
        squads = Squad.objects.all()
        serialized_squads = SquadSerializer(squads, many=True)

        return Response(serialized_squads.data, status=status.HTTP_200_OK)
