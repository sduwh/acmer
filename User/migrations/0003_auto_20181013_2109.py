# Generated by Django 2.1.2 on 2018-10-13 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20181013_2023'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('real_name', 'student_id', 'school')},
        ),
    ]