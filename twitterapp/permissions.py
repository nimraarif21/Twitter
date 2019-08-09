from django.contrib.auth.models import User
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(pk=obj.pk)
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == user
   

class IsOwnerOrCreateOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = User.objects.get(pk=obj.pk)
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True
        return request.user == user
