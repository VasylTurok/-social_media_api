import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


class Profile(models.Model):
    username = models.CharField(
        max_length=64,
        unique=True,
        default="username"
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True
    )
    biography = models.TextField(blank=True)

    def follow(self, profile) -> None:
        self.following.add(profile)

    def unfollow(self, profile) -> None:
        self.following.remove(profile)


def post_image_path(instance, filename):
    _, extension = os.path.splitext(filename)
    return os.path.join(
        "uploads/posts/",
        f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"
    )


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(null=True, upload_to=post_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        Profile,
        related_name="post_liked",
        blank=True
    )
    scheduled_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.created_at}"

    class Meta:
        ordering = ("-created_at",)


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
