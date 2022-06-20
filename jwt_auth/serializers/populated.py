from squad.serializers.common import SquadSerializer

from .members import CommonUserSerializer


class PopulatedUserSerializer(CommonUserSerializer):
    squads = SquadSerializer(many=True)
