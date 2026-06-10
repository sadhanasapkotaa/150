from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="following"
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    likes = models.IntegerField()
    repost = models.IntegerField()

    @property
    def __str__(self):
        return self.title[:10] + self.user.first_name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentor")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commented_post"
    )
    comment = models.CharField(max_length=5000)
    comment_likes = models.IntegerField()

    def __str__(self):
        return self.comment[:10]
