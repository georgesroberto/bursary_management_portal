from functools import wraps
from django.shortcuts import redirect

def check_group_permission(group_names):
    """
    Custom decorator to check if the user belongs to specified groups.
    Args:
        group_names (list): List of group names to check.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if any(user.groups.filter(name=group_name).exists() for group_name in group_names):
                return view_func(request, *args, **kwargs)
            else:
                return redirect('permission_denied_view')

        return _wrapped_view

    return decorator
