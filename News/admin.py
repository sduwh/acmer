from django.contrib import admin
from imagekit.admin import AdminThumbnail
from News.models import News, NewsPhotos
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'actor_username', 'create_time', 'news_type')
    list_filter = ('create_time', 'news_type')
    fieldsets = (
        (None, {
            'fields': ('title', 'actor', 'news_type', 'content')
        }),
    )
    search_fields = ('title', 'actor', 'create_time')
    ordering = ('title', 'create_time')
    filter_horizontal = ()

    # 在admin中显示文章的作者名
    @staticmethod
    def actor_username(obj):
        username = obj.actor.username
        return username


class NewsPhotoAdmin(admin.ModelAdmin):
    list_display = ('describe', 'image_thumbnail', 'actor_username', 'create_time')
    list_filter = ('create_time', 'actor')
    fieldsets = (
        (None, {
            'fields': ('img', 'describe', 'actor')
        }),
    )
    search_fields = ('describe', 'actor_username', 'create_time')
    ordering = ('create_time',)
    filter_horizontal = ()

    image_thumbnail = AdminThumbnail(image_field='img_thumbnail')

    # 在admin中显示上传图片的作者名
    @staticmethod
    def actor_username(obj):
        username = obj.actor.username
        return username


admin.site.register(News, NewsAdmin)
admin.site.register(NewsPhotos, NewsPhotoAdmin)