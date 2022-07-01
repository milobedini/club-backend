from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from squad.models import Squad

from posts.serializers.common import PostSerializer

from .models import Post
from .serializers.populated import PopulatedPostSerializer


# Create your views here.
class PostsListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        # may need to add check so only a squad member can see and make posts.
        try:
            squad = Squad.objects.get(pk=pk)
        except Squad.DoesNotExist:
            raise NotFound("Club not found.")

        # check user in squad
        check_for_user = squad.members.filter(id=request.user.id)
        if len(check_for_user) == 0:
            raise PermissionDenied(detail="You must be a member of this club in order to see the feed.")

        posts = Post.objects.filter(club=pk)
        serialized_posts = PopulatedPostSerializer(posts, many=True)
        return Response(serialized_posts.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        request.data["owner"] = request.user.id
        request.data["club"] = pk
        post_to_create = PostSerializer(data=request.data)
        if post_to_create.is_valid():
            post_to_create.save()
            return Response(post_to_create.data, status=status.HTTP_201_CREATED)
        return Response(post_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PostDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk, id):
        try:
            post_to_delete = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise NotFound(detail="Post not found.")
        if post_to_delete.owner != request.user:
            raise PermissionDenied(detail="User does not own this note.")
        post_to_delete.delete()
        return Response({"Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
