# Generated by Django 2.1.2 on 2018-10-15 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20181013_2109'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
    ]
