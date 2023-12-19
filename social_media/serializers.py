from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import gettext as _
from social_media.models import Post, Comment, Profile


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("author", "post", "content", "created_at")
        read_only_fields = ("id", "author", "created_at")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("username", "profile_image", "biography")

    def validate(self, attrs):
        user = self.context["request"].user
        profile = self.instance

        if profile and profile == user.profile:
            raise serializers.ValidationError("You cannot follow yourself.")
        if profile and profile in user.profile.following.all():
            raise serializers.ValidationError("You are already following this profile.")

        return attrs

    def follow(self, target_profile):
        user_profile = self.context["request"].user.profile
        if user_profile != target_profile and target_profile not in user_profile.following.all():
            user_profile.follow(target_profile)
        else:
            raise serializers.ValidationError("Unable to follow the profile.")

    def unfollow(self, target_profile):
        user_profile = self.context["request"].user.profile
        if user_profile != target_profile and target_profile in user_profile.following.all():
            user_profile.unfollow(target_profile)
        else:
            raise serializers.ValidationError("Unable to unfollow the profile.")


class ProfileListSerializer(ProfileSerializer):
    followers = serializers.IntegerField(source="followers.count")
    following = serializers.IntegerField(source="following.count")

    class Meta:
        model = Profile
        fields = (
            "username",
            "profile_image",
            "biography",
            "followers",
            "following"
        )


class ProfileDetailSerializer(ProfileSerializer):
    followers = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username"
    )
    following = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="username"
    )

    class Meta:
        model = Profile
        fields = (
            "username",
            "profile_image",
            "biography",
            "followers",
            "following"
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "author",
            "scheduled_time",
            "post_image"
        )
        read_only_fields = ("id", "author",)

    def validate(self, attrs) -> dict:
        user = self.context["request"].user.profile
        attrs["author"] = user
        return attrs


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    comments = serializers.IntegerField(source="comments.count", read_only=True)
    likes = serializers.IntegerField(source="likes.count", read_only=True)
    write_only_fields = ("scheduled_time",)

    class Meta:
        model = Post
        fields = (
            "author",
            "title",
            "content",
            "created_at",
            "post_image",
            "comments",
            "likes",
            "scheduled_time"
        )


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.IntegerField(source="likes.count", read_only=True)
    write_only_fields = ("scheduled_time",)

    class Meta:
        model = Post
        fields = (
            "author",
            "title",
            "content",
            "created_at",
            "post_image",
            "comments",
            "likes",
            "scheduled_time",
        )


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("post_image",)
