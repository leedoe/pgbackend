# Generated by Django 3.1 on 2020-09-03 14:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20200903_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]