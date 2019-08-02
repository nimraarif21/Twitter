from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models.tweet import Tweet
from .models.userrelation import Userrelation

class UserSerializer(serializers.ModelSerializer):
    # tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all()) 
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['id', 'username', 'email', 'password']


class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tweet   
        fields = ['id', 'content', 'owner', 'createdat']


class UserRelationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source ='user.id')

    class Meta:
        model = Userrelation
        fields = ['id', 'user', 'following', 'createdat']


