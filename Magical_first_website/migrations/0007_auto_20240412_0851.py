# Generated by Django 3.2.22 on 2024-04-12 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Magical_first_website', '0006_auto_20240412_0806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_in_magical_website',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user_in_magical_website',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='user_in_magical_website',
            old_name='username',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user_in_magical_website',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user_in_magical_website',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user_in_magical_website',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user_in_magical_website',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user_in_magical_website',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user_in_magical_website',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user_in_magical_website',
            name='last_name',
        ),
    ]
