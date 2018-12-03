from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from Activity.models import Team, Game, Person


# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = (
        'headline',
        'game_type',
        'game_time',
        'start_enter_time',
        'end_enter_time',
        'actor',
        'img_thumbnail',
        # 'create_time'
    )
    list_filter = ('headline', 'game_type',)
    search_fields = ('headline',)
    ordering = ('game_time',)
    filter_horizontal = ()


class PersonInline(admin.TabularInline):
    model = Person
    extra = 0
    verbose_name = "队员"


def verify(modeladmin, request, queryset):
    queryset.update(is_verify=True)


verify.short_description = "确认审核"


# django-import-export
class TeamResource(resources.ModelResource):
    def get_export_headers(self):
        # 是你想要的导出头部标题headers
        return ['人员', '邮箱', '学号', '学校', '电话', '专业', '队名/人名', '指导老师']

    persons = Field()
    email = Field()
    stu_id = Field()
    school = Field()
    phone = Field()
    major = Field()

    class Meta:
        model = Team
        fields = ('team_name', 'teacher')

    @staticmethod
    def dehydrate_persons(obj):
        re = ""
        for index, obj in enumerate(obj.persons.all()):
            re += str(index + 1) + '、' + obj.user_name
            re = re + "\n"
        return re

    @staticmethod
    def dehydrate_email(obj):
        re = ""
        for index, obj in enumerate(obj.persons.all()):
            re += str(index + 1) + '、' + obj.email
            re = re + "\n"
        return re

    @staticmethod
    def dehydrate_phone(obj):
        re = ""
        for index, obj in enumerate(obj.persons.all()):
            re += str(index + 1) + '、' + str(obj.phone)
            re = re + "\n"
        return re

    @staticmethod
    def dehydrate_stu_id(obj):
        re = ""
        for index, obj in enumerate(obj.persons.all()):
            re += str(index + 1) + '、' + str(obj.student_id)
            re = re + "\n"
        return re

    @staticmethod
    def dehydrate_major(obj):
        re = ""
        for index, obj in enumerate(obj.persons.all()):
            re += str(index + 1) + '、' + obj.major
            re = re + "\n"
        return re

    @staticmethod
    def dehydrate_school(obj):
        return obj.persons.all().first().school.school_name


class TeamAdmin(ImportExportActionModelAdmin):
    list_display = ('team_name', 'teacher', 'game_name', 'is_verify', 'all_persons')
    list_filter = ('game__headline', 'teacher',)
    search_fields = ('team_name',)
    ordering = ('team_name',)
    filter_horizontal = ()
    inlines = [
        PersonInline,
    ]
    actions = [verify]

    resource_class = TeamResource

    @staticmethod
    def game_name(obj):
        game_name = obj.game.headline
        return game_name

    @staticmethod
    def all_persons(obj):
        re = []
        for i in obj.persons.all():
            re.append(i.user_name)
        return re

    all_persons.allow_tags = True
    all_persons.short_description = "队长"


admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
