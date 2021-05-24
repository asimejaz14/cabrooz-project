# Generated by Django 3.2.3 on 2021-05-24 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0001_initial'),
        ('user', '0006_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.ForeignKey(blank=True, default=1, max_length=200, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='option.option'),
        ),
    ]
