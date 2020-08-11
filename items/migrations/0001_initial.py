# Generated by Django 3.0.5 on 2020-08-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('thumbnail', models.URLField()),
                ('price', models.IntegerField()),
                ('link', models.URLField()),
                ('soldout', models.BooleanField()),
                ('store_name', models.CharField(max_length=191)),
            ],
        ),
    ]
