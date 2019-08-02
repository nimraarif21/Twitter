from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from .models.tweet import Tweet
from .models.userrelation import Userrelation
from .serializers import UserSerializer, TweetSerializer, UserrelationSerializer
from .permissions import IsOwnerOrReadOnly

class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TweetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class UserRelationCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    queryset = Userrelation.objects.all()
    serializer_class = UserrelationSerializer

class UserRelation(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Userrelation.objects.all()
    serializer_class = UserrelationSerializer








