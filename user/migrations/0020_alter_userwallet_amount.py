# Generated by Django 3.2.3 on 2021-05-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20210529_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='amount',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
    ]