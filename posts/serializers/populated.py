from jwt_auth.serializers.common import CommonUserSerializer

from .common import PostSerializer


class PopulatedPostSerializer(PostSerializer):
    owner = CommonUserSerializer()
