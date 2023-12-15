# Generated by Django 4.0.4 on 2023-12-15 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import social_media.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=64, unique=True)),
                ('biography', models.TextField(blank=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='following', to='social_media.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=social_media.models.post_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_time', models.DateTimeField(blank=True, null=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_liked', to='social_media.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social_media.profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social_media.post')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]