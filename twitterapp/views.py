from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from .models.tweet import Tweet
from .models.userRelation import UserRelation
from .models.like import TweetLike
from .models.comment import Comment
from .serializers import UserSerializer, TweetSerializer, UserRelationSerializer, FollowingSerializer, FollowerSerializer, LikeSerializer, CommentSerializer, NewsFeedSerializer
from .permissions import IsOwnerOrReadOnly, IsOwnerOrCreateOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrCreateOnly]


class TweetViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def update(self, serializer):
    #     serializer.save(owner=self.request.user)


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NewsFeedSerializer
    def get_queryset(self):
        user = self.request.user
        following = UserRelation.objects.filter(owner=user).values_list('following', flat=True)
        return Tweet.objects.filter(owner__in=following)


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
