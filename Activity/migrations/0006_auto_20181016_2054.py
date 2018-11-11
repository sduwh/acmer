# Generated by Django 2.1.2 on 2018-10-16 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0005_auto_20181015_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': '比赛'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': '队伍'},
        ),
        migrations.AddField(
            model_name='game',
            name='pay_money',
            field=models.IntegerField(default=0, verbose_name='报名费'),
        ),
        migrations.AddField(
            model_name='game',
            name='qr_code',
            field=models.ImageField(default=None, upload_to='upload/QR/%Y/%m/%d', verbose_name='图片（建议size为100*100）'),
        ),
        migrations.AddField(
            model_name='game',
            name='require_pay',
            field=models.BooleanField(default=False, verbose_name='需要支付'),
        ),
        migrations.AddField(
            model_name='team',
            name='is_verify',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='审核'),
        ),
        migrations.AlterField(
            model_name='game',
            name='headline',
            field=models.CharField(default='', max_length=256, verbose_name='比赛名称'),
        ),
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='persons', related_query_name='person', to='Activity.Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='game',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Activity.Game', verbose_name='比赛'),
        ),
        migrations.AlterField(
            model_name='team',
            name='teacher',
            field=models.CharField(blank=True, default=' ', max_length=256, null=True, verbose_name='指导老师'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(default='', max_length=256, null=True, verbose_name='队名'),
        ),
    ]
