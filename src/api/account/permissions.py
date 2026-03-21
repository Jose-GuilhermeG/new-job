from rest_framework.permissions import IsAuthenticated


class IsProfileOwner(
    IsAuthenticated
):

    def has_object_permission(self, request, view, obj):
        return request.user.pk == obj.user.pk
