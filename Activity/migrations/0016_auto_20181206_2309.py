# Generated by Django 2.1.3 on 2018-12-06 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0015_auto_20181019_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': '活动', 'verbose_name_plural': '活动'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': '队伍/个人', 'verbose_name_plural': '队伍/个人'},
        ),
    ]
