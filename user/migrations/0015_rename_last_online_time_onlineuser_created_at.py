# Generated by Django 3.2.3 on 2021-05-29 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_onlineuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlineuser',
            old_name='last_online_time',
            new_name='created_at',
        ),
    ]
