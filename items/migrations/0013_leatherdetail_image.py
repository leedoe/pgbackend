# Generated by Django 3.1 on 2020-09-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_auto_20200916_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='leatherdetail',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]