# Generated by Django 5.1.1 on 2024-11-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='exmaple-slug', unique=True),
            preserve_default=False,
        ),
    ]