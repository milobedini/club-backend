from events.serializers.common import EventSerializer
from events.serializers.populated import PopulatedEventSerializer
from squad.serializers.common import SquadSerializer

from .members import CommonUserSerializer


class PopulatedUserSerializer(CommonUserSerializer):
    squads = SquadSerializer(many=True)
    admin_squads = SquadSerializer(many=True)
    attending = PopulatedEventSerializer(many=True)
    squad_requests = SquadSerializer(many=True)
