# Generated by Django 3.0.5 on 2020-06-16 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191)),
                ('content', models.TextField()),
                ('writer_name', models.CharField(max_length=191)),
                ('noticed', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('writer', models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_name', models.CharField(max_length=191)),
                ('deleted', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Post')),
                ('writer', models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
