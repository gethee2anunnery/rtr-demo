from django.contrib import admin

from shortlinks.models import ShortLink, RequestData


class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('link_text', 'target')
    search_fields = ('link_text', 'target')

admin.site.register(ShortLink, ShortLinkAdmin)
admin.site.register(RequestData)
