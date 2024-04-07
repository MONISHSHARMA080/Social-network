# Generated by Django 3.2.22 on 2024-04-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('network', '0005_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='network_users', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_name='network_user_permissions', to='auth.Permission'),
        ),
    ]