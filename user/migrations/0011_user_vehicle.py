# Generated by Django 3.2.3 on 2021-05-29 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
        ('user', '0010_alter_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vehicle_id', to='vehicle.vehicle'),
        ),
    ]