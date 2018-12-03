from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.


class History(models.Model):
    # 历程类
    id = models.AutoField(primary_key=True)
    game = models.CharField(max_length=256,
                            default='')
    date = models.DateField(null=False,
                            blank=False,
                            verbose_name="比赛时间")
    achievement = models.CharField(max_length=256,
                                   verbose_name="成就")
    img = models.ImageField(verbose_name="比赛照片一张",
                            upload_to='upload/%Y/%m/%d',
                            max_length=100)
    img_thumbnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(80, 45)],
        format='JPEG',
        options={
            'quality': 60,
        }
    )
    img_show = ImageSpecField(
        source='img',
        processors=[ResizeToFill(487, 324)],
        format='JPEG',
        options={
            'quality': 60,
        }
    )
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game

    class Meta:
        verbose_name = "历程"
        verbose_name_plural = verbose_name


class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='队员',
                             related_name='team_member')

    def __str__(self):
        return self.user.__str__()

    class Meta:
        db_table = 'TeamMember'
        verbose_name = "队员信息"
        verbose_name_plural = verbose_name


class GameRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TeamMember', on_delete=models.DO_NOTHING, verbose_name='队员', related_name='game_record')
    game = models.CharField(max_length=125, default='', verbose_name='比赛名称')
    result = models.CharField(max_length=125, default='', verbose_name='比赛结果')
    game_time = models.DateTimeField(default=None, verbose_name='比赛时间')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'GameRecord'
        verbose_name = "比赛记录"
        verbose_name_plural = verbose_name
