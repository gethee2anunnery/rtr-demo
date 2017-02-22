from django.contrib import admin

from shortlinks.models import ShortLink, RequestData


class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('link_text', 'target', 'request_count')
    search_fields = ('link_text', 'target', 'request_count')
    readonly_fields = ('request_count',)

    def request_count(self, obj):
        return obj.requestdata_set.count()


class RequestDataAdmin(admin.ModelAdmin):
    list_display = ('remote_addr', 'shortlink', 'time')
    search_fields = ('remote_addr', 'path', 'uri')
    sort_fields = ('remote_addr', 'path', 'uri')
    readonly_fields = ('shortlink', 'time', 'remote_addr',
                       'path', 'uri', 'user_agent')


admin.site.register(ShortLink, ShortLinkAdmin)
admin.site.register(RequestData, RequestDataAdmin)
