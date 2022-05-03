from rest_framework import permissions


class IsAuthorOrModeratorOrAdminOrReadOnly(permissions.BasePermission):
    """Настройки доступа.

    Доступ на чтение любому пользователю.
    Доступ на запись аутентифицированным пользователям.
    Редактирование, удаление - только для автора, модератора, администратора
    или суперюзера.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.role == 'moderator'
            or request.user.is_stuff
            or request.user.is_superuser
        )
