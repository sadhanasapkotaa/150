from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .models import Comment, Post, User
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostByUserViewSet(ModelViewSet):
    queryset = Post.objects.select_related("user")
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentByPostViewset(ModelViewSet):
    queryset = Comment.objects.select_related("post")
    serializer_class = CommentSerializer


class CommentByUserViewset(ModelViewSet):
    queryset = Comment.objects.select_related("user")
    serializer_class = CommentSerializer
