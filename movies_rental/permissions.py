from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def has_object_permission(self, request, view, obj):
		# Read permission are allowed to any request
		# so we'll always allow GET, HEAD or OPTIONS request.
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the owner of the snippet.
		return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow admin users to have full access.
	"""

	def has_permission(self, request, view):
		if request.user and request.user.is_staff:
			return True
		if view.action in ['list', 'retrieve', 'create']:
			return True
		return False