# Generated by Django 3.1 on 2020-09-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_comment_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leather',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leatherdetail',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tannery',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
