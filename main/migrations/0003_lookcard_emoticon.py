# Generated by Django 5.2 on 2025-06-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_like_comment_likes_remove_comment_dislike_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookcard',
            name='emoticon',
            field=models.ImageField(blank=True, null=True, upload_to='emoticons/'),
        ),
    ]
