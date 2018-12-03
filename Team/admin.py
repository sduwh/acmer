from django.contrib import admin
from .models import History, TeamMember, GameRecord
from imagekit.admin import AdminThumbnail


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['game', 'date', 'img_thumbnail', 'achievement']
    list_filter = ['game', 'date']
    img_thumbnail = AdminThumbnail(image_field='img_thumbnail')
    ordering = ('create_time',)
    search_fields = ('game', 'date',)
    filter_horizontal = ()


class GameRecordInline(admin.TabularInline):
    model = GameRecord
    extra = 0
    verbose_name = '比赛记录'


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_grade', 'user_major']
    list_filter = ['user']
    ordering = ('id',)
    inlines = [GameRecordInline]

    @staticmethod
    def user_grade(obj):
        return obj.user.grade

    @staticmethod
    def user_major(obj):
        return obj.user.major


class GameRecordAdmin(admin.ModelAdmin):
    list_filter = ['user', 'game', 'result', 'game_time']
    list_display = ['user', 'game', 'result', 'game_time']
    ordering = ('create_time',)
    search_fields = ('game', 'game_tme', 'user')


admin.site.register(History, HistoryAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(GameRecord, GameRecordAdmin)
