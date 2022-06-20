from ...squad.serializers.common import SquadSerializer
from .favourite import CommonUserSerializer


class PopulatedUserSerializer(CommonUserSerializer):
    squads = SquadSerializer(many=True)
