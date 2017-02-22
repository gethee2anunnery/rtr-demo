from django.shortcuts import render


from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect

from .models import ShortLink

def shortlink_redirect( request, link_text ):
    link_text = link_text.replace('/','');
    url = get_object_or_404( ShortLink, link_text=link_text )
    return HttpResponseRedirect( url.target )
