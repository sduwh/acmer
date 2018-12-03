from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from User.models import User

# Create your models here.


class News(models.Model):
    # 动态类的模型
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    actor = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        limit_choices_to={'is_admin': True}
    )
    type_choice = (
        ("0", '通讯'),
        ("1", '通知')
    )
    news_type = models.CharField(
        choices=type_choice,
        default='0',
        max_length=16
    )
    content = RichTextUploadingField(
        config_name='default',
        default='',
    )
    USERNAME_FIELD = 'title'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = verbose_name


class NewsPhotos(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(
        verbose_name="图片（建议size为800*450）",
        upload_to='upload/%Y/%m/%d',
        max_length=100,
    )
    # admin后台缩略图
    img_thumbnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(80, 45)],
        format="JPEG",
        options={
            'quality': 60
        }
    )
    # 前端展示
    img_show = ImageSpecField(
        source='img',
        processors=[ResizeToFill(800, 450)],
        format="JPEG",
        options={
            'quality': 60
        }
    )
    describe = models.TextField(verbose_name="描述")
    create_time = models.DateTimeField(auto_now_add=True)
    actor = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        limit_choices_to={'is_admin': True},
    )

    def __str__(self):
        return self.describe

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
