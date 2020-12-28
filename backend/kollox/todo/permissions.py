from rest_framework.permissions import BasePermission
from .models import Project, SimpleToDoList

class ListOwnerPermission(BasePermission):
    """
    Check if current user is owner of todolist
    or owner share this list to current user
    """

    def has_permission(self, request, view):
        list_id = view.kwargs.get('id', None)
        request_params = str(view.request.parser_context["view"].request)
        route = request_params[request_params.index("'"): -1]
        if route.find("project") > 0:
            _list = Project.objects.get(id=list_id)
        else:
            _list = SimpleToDoList.objects.get(id=list_id)

        if _list.owner == request.user:
            return True

        if request.user in _list.shared_owners.all():
            return True
