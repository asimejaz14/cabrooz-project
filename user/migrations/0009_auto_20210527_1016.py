# Generated by Django 3.2.3 on 2021-05-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cnic_back',
            field=models.ImageField(blank=True, null=True, upload_to='user/documents/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cnic_front',
            field=models.ImageField(blank=True, null=True, upload_to='user/documents/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='license_back',
            field=models.ImageField(blank=True, null=True, upload_to='user/documents/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='license_front',
            field=models.ImageField(blank=True, null=True, upload_to='user/documents/'),
        ),
    ]
