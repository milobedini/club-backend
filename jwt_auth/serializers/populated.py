from events.serializers.common import EventSerializer
from squad.serializers.common import SquadSerializer

from .members import CommonUserSerializer


class PopulatedUserSerializer(CommonUserSerializer):
    squads = SquadSerializer(many=True)
    admin_squads = SquadSerializer(many=True)
    attending = EventSerializer(many=True)
