# Generated by Django 4.2.6 on 2023-10-10 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_rename_followers_network_follower_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
    ]