from jwt_auth.serializers.common import CommonUserSerializer

from .common import SquadSerializer


class PopulatedSquadSerializer(SquadSerializer):
    members = CommonUserSerializer(many=True)
    admin_members = CommonUserSerializer(many=True)
