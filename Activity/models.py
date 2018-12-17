from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from datetime import datetime


class Person(models.Model):
    # 队员 个人赛队员人数为1 团队赛人数为3
    id = models.AutoField(primary_key=True)
    is_captain = models.BooleanField(default=False)
    user_name = models.CharField(
        max_length=256,
        default="",
        null=False
    )
    student_id = models.BigIntegerField()
    email = models.EmailField(
        unique=False,
        verbose_name='email asdaddress',
        max_length=256
    )
    phone = models.BigIntegerField()
    major = models.CharField(
        max_length=56,
        default="",
        null=True
    )
    school = models.ForeignKey(
        'User.School',
        on_delete=models.DO_NOTHING,
        default=None
    )
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        default=None,
        related_name='persons',
        related_query_name='person'
    )

    def __str__(self):
        return self.user_name


class Team(models.Model):
    # 队名，指导老师，活动/比赛
    id = models.AutoField(primary_key=True)
    team_name = models.CharField(
        max_length=256,
        default='',
        null=True,
        verbose_name="队名/个人名称"
    )
    teacher = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        default=" ",
        verbose_name='指导老师'
    )
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        default=None,
        verbose_name="比赛"
    )

    def __str__(self):
        return "活动/个人"

    is_verify = models.BooleanField(
        blank=True,
        default=False,
        verbose_name="通过审核"
    )

    class Meta:
        verbose_name = "队伍/个人"
        verbose_name_plural = verbose_name


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(
        max_length=256,
        null=False,
        default='',
        verbose_name="活动名称"
    )
    describe = models.TextField(
        null=True,
        default=''
    )
    type_choice = (
        ('0', '团队'),
        ('1', '个人')
    )
    game_type = models.CharField(
        choices=type_choice,
        default='0',
        max_length=16,
        verbose_name="类型"
    )
    # 活动/比赛 时间
    game_time = models.DateTimeField(verbose_name="活动时间")
    # 报名开始截止时间
    start_enter_time = models.DateTimeField(verbose_name="报名开始时间")
    end_enter_time = models.DateTimeField(verbose_name="报名截止时间")

    location = models.CharField(
        max_length=256,
        null=True,
        blank=False,
        default="",
        verbose_name="活动地点"
    )

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        limit_choices_to={'is_admin': True}
    )

    require_pay = models.BooleanField(
        default=False,
        verbose_name="需要支付"
    )
    pay_money = models.IntegerField(
        verbose_name="报名费",
        default=0
    )

    img = models.ImageField(
        verbose_name="图片（建议size为100*100）",
        upload_to='upload/QR/%Y/%m/%d',
        max_length=100,
        default=None,
        blank=True
    )
    # admin后台缩略图
    img_thumbnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={
            'quality': 60
        }
    )
    # 前端展示
    img_show = ImageSpecField(
        source='img',
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={
            'quality': 60
        }
    )
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = verbose_name
