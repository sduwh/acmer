# Generated by Django 2.1.2 on 2018-10-13 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(default='', max_length=256)),
            ],
            options={
                'db_table': 'School',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='User.School'),
        ),
    ]