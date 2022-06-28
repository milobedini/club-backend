from jwt_auth.serializers.common import CommonUserSerializer
from squad.serializers.common import SquadSerializer

from .common import EventSerializer


class PopulatedEventSerializer(EventSerializer):
    club = SquadSerializer()
    participants = CommonUserSerializer(many=True)
    financier = CommonUserSerializer()
