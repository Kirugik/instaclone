# Generated by Django 4.0.5 on 2022-06-03 13:03

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
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=100)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-posted_on'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/')),
                ('image_name', models.CharField(max_length=100)),
                ('image_caption', models.TextField(blank=True, max_length=200, null=True)),
                ('posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, upload_to='profile_images/')),
                ('bio', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoapp.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoapp.profile'),
        ),
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoapp.comment'),
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoapp.like'),
        ),
        migrations.AddField(
            model_name='comment',
            name='image_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoapp.image'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]