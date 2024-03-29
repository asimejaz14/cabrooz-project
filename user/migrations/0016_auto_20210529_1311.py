# Generated by Django 3.2.3 on 2021-05-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_rename_last_online_time_onlineuser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineuser',
            name='current_latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='onlineuser',
            name='current_longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
    ]
