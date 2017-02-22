from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.utils.translation import ugettext_lazy as _


class ShortLink(models.Model):
    link_text = models.SlugField( _("Short Link Text"), max_length = 20,
        unique = True, help_text=_("Given the domain 'rtr.co', enter your shortlink "
                                   "text without slashes or spaces. "
                                   "Ex: 'red-dress'.") )
    target = models.URLField( _("Target URL"), max_length = 255,
        help_text=_("Enter a valid URL, including domain, where you "
                                   "want the shortlink to redirect to. "
                                   "Ex: http://www.renttherunway.com/the-really-long-"
                                   "link-to-the-red-dress-PDP"))


    def __unicode__(self):
        return "%s ---> %s" % (self.link_text, self.target)

    class Meta:
        unique_together=(('link_text', 'target'),)
        ordering = ('link_text',)


class RequestData(models.Model):
    shortlink = models.ForeignKey(ShortLink)
    time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=1000)
    uri = models.CharField(max_length=2000)
    user_agent = models.CharField(max_length=1000,blank=True,null=True)
    remote_addr = models.GenericIPAddressField()

    def __unicode__(self):
        return "%s ---> %s" % (self.remote_addr)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Request Data'
