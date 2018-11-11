from django.db import models
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
