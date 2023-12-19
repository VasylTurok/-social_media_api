from rest_framework.permissions import BasePermission


class IsProfileOwnerOrGetMethod(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return request.method == "GET" or obj.user == request.user


class IsPostOwnerOrGetMethod(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return request.method == "GET" or obj.author == request.user.profile