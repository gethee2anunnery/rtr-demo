import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .models import ShortLink, RequestData

def shortlink_redirect( request, link_text ):
    link_text = link_text.replace('/','');
    url = get_object_or_404( ShortLink, link_text=link_text )

    # create a new RequestData object for analytics
    try:
        meta = request.META.copy()

        RequestData(
            shortlink = url,
            path = request.path,
            uri = request.build_absolute_uri(),
            user_agent = meta.pop('HTTP_USER_AGENT',None),
            remote_addr = meta.pop('REMOTE_ADDR',None),
        ).save()

    except Exception as e:
        print e

    return HttpResponseRedirect( url.target )
