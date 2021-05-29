# Generated by Django 3.2.3 on 2021-05-29 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0001_initial'),
        ('vehicle', '0003_auto_20210529_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='option.option'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vehicle_category_id', to='option.option'),
        ),
    ]