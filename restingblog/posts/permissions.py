from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allw authors of an objects to edit it.
	"""

	def has_object_permission(self, request, view, obj):
		#Reaad permissions are allowed to any request,
		#so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permission.SAFE_METHODS:
			return True

		#write permisssions are allowed only to author of the post
		return obj.author == request.user

		