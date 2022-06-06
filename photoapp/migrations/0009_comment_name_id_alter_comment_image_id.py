# Generated by Django 4.0.5 on 2022-06-06 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0008_image_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_comments', to='photoapp.image'),
        ),
    ]
