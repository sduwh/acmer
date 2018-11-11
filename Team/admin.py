from django.contrib import admin
from .models import History
from imagekit.admin import AdminThumbnail
# Register your models here.


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['game', 'date', 'img_thumbnail', 'achievement']
    list_filter = ['game', 'date']
    img_thumbnail = AdminThumbnail(image_field='img_thumbnail')
    ordering = ('create_time',)
    search_fields = ('game', 'date',)
    filter_horizontal = ()


admin.site.register(History, HistoryAdmin)
