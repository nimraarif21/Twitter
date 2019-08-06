from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .models.tweet import Tweet
from .models.userRelation import UserRelation
from .models.like import TweetLike
from .serializers import UserSerializer, TweetSerializer, UserRelationSerializer, FollowingSerializer, FollowerSerializer, LikeSerializer
from .permissions import IsOwnerOrReadOnly


class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TweetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class UserRelationCreateList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset = UserRelation.objects.all()
    serializer_class = UserRelationSerializer


class UserRelationUpdate(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = UserRelation.objects.all()
    serializer_class = UserRelationSerializer


class FollowingList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowingSerializer

    def get_queryset(self):
        user = self.request.user
        return UserRelation.objects.filter(user=user)


class FollowerList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        user = self.request.user
        return UserRelation.objects.filter(following=user)


class LikeaTweet(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = TweetLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UnlikeaTweet(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = TweetLike.objects.all()


class NewsFeed(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = TweetSerializer

    def get_queryset(self):
        user = self.request.user
        following = UserRelation.objects.filter(user=user).values_list('following', flat=True)
        return Tweet.objects.filter(owner__in=following)
