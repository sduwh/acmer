# Generated by Django 2.1.4 on 2018-12-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20181206_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(blank=True, null=True, verbose_name='年级'),
        ),
    ]
