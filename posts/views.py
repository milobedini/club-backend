from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers.populated import PopulatedPostSerializer


# Create your views here.
class PostsListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        # may need to add check so only a squad member can see posts?
        posts = Post.objects.filter(club=pk)
        serialized_posts = PopulatedPostSerializer(posts, many=True)
        return Response(serialized_posts.data, status=status.HTTP_200_OK)
