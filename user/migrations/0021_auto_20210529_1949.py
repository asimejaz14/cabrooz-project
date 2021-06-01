# Generated by Django 3.2.3 on 2021-05-29 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0001_initial'),
        ('user', '0020_alter_userwallet_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlineuser',
            old_name='current_longitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='onlineuser',
            old_name='current_latitude',
            new_name='longitude',
        ),
        migrations.RemoveField(
            model_name='onlineuser',
            name='distance',
        ),
        migrations.AddField(
            model_name='onlineuser',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='onlineuser',
            name='is_online',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='onlineuser',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserLiveLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_online', models.BooleanField(blank=True, default=False, max_length=200, null=True)),
                ('current_longitude', models.DecimalField(blank=True, decimal_places=19, max_digits=19, null=True)),
                ('current_latitude', models.DecimalField(blank=True, decimal_places=19, max_digits=19, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('distance', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='option.option')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
