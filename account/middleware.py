from django.http import HttpResponseRedirect
from django.urls import reverse


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Here I call login if not authenticated and request is not login page
        if not request.user.is_authenticated and request.path != (reverse('account:login')) and request.path != (reverse('account:forget_password')):
            return HttpResponseRedirect(reverse('account:login'))  
        response = self.get_response(request)
        return response