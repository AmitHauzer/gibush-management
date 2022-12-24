from django.contrib import messages
from functools import wraps
from urllib.parse import urlparse
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, resolve_url


def user_passes_test(
    test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME
):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            test_result = test_func(request.user)
            if test_result:
                return view_func(request, *args, **kwargs)
            elif test_result == False:
                messages.error(request,'Authentication Error: Login required')
            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if (not login_scheme or login_scheme == current_scheme) and (
                not login_netloc or login_netloc == current_netloc
            ):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login

            return redirect_to_login(path, resolved_login_url, redirect_field_name)

        return _wrapped_view

    return decorator


def login_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None
):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        @login_required
        def wrapper_func(request,*args,**kwargs):
            
            groups = []
            if request.user.groups.exists():
                for group in request.user.groups.all():
                    groups.append(group.name)
                # print("User's groups: ",groups)
                # print("Allowed role:  ",allowed_roles)
                # result = any(group in allowed_roles for group in groups)
                # print("Allowed?       ",result)
            if any(group in allowed_roles for group in groups):
                return view_func(request,*args,**kwargs)
            if request.user.is_staff:
                return view_func(request,*args,**kwargs)
            else:
                messages.error(request, "You are not allowed.")
                return redirect("home-page")
        return wrapper_func
    return decorator

# def permission_required(perm, login_url=None, raise_exception=False):
#     """
#     Decorator for views that checks whether a user has a particular permission
#     enabled, redirecting to the log-in page if necessary.
#     If the raise_exception parameter is given the PermissionDenied exception
#     is raised.
#     """

#     def check_perms(user):
#         if isinstance(perm, str):
#             perms = (perm,)
#         else:
#             perms = perm
#         # First check if the user has the permission (even anon users)
#         if user.has_perms(perms):
#             return True
#         # In case the 403 handler should be called raise the exception
#         if raise_exception:
#             raise PermissionDenied
#         # As the last resort, show the login form
#         return False

#     return user_passes_test(check_perms, login_url=login_url)
