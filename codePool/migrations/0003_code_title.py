# Generated by Django 2.1.3 on 2018-12-06 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codePool', '0002_auto_20181205_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='title',
            field=models.CharField(default='', max_length=256, verbose_name='标题'),
        ),
    ]
