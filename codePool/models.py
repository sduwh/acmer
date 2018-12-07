from django.db import models
from django.conf import settings


class Code(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='code',
                             verbose_name='作者')
    title = models.CharField(max_length=256, default='', verbose_name='标题')
    code = models.TextField(verbose_name='代码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_share = models.BooleanField(default=False, verbose_name='是否分享')

    class Meta:
        db_table = 'Code'
        verbose_name = '码池'
        verbose_name_plural = verbose_name
