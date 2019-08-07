from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models.tweet import Tweet
from .models.userRelation import UserRelation
from .models.like import TweetLike
from .models.comment import Comment


class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['id', 'username', 'email', 'password']


class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Tweet   
        fields = ['id', 'content', 'owner', 'created_at']


class UserRelationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = UserRelation
        fields = ['id', 'owner', 'following']


class FollowingSerializer(serializers.ModelSerializer):
    following = UserSerializer()

    class Meta:
        model = UserRelation
        fields = ['following']


class FollowerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserRelation
        fields = ['user']


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')

    class Meta:
        model = TweetLike  
        fields = ['id', 'owner', 'tweet']



class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'owner', 'tweet', 'created_at']


class NewsFeedSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.likes.count()

    class Meta:
        model = Tweet   
        fields = ['id', 'content', 'owner', 'likes', 'comments', 'created_at']

