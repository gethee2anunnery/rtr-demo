from django.http import Http404
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from .views import shortlink_redirect


class ShortLinkMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        if response.status_code != 404:
             # No need to check these.
            return response

        try:
            return shortlink_redirect(request, request.path_info)

        # if this fails, return the original response
        # and/or log the error
        except Http404:
            return response
        except Exception as e:
            if settings.DEBUG:
                print e
            return response
