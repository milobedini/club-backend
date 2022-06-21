from jwt_auth.serializers.common import CommonUserSerializer

from .common import EventSerializer


class PopulatedEventSerializer(EventSerializer):
    participants = CommonUserSerializer(many=True)
    financier = CommonUserSerializer()
