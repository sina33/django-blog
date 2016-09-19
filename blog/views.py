from django.http import HttpResponse
from rest_framework import generics

from blog.models import Post, User
from blog.serializers import PostSerializer, UserSerializer


def index(request):
    return HttpResponse("You're at the blog index.")


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
