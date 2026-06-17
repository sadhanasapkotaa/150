from rest_framework import serializers

from .models import Comment, Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    first_name = serializers.CharField(source="user.first_name")
    comment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "likes",
            "repost",
            "email",
            "first_name",
            "comment_count",
        ]

    def get_comment_count(self, instance):
        return instance.comments.count()
