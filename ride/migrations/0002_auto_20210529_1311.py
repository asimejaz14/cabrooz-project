# Generated by Django 3.2.3 on 2021-05-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='accepted_at_latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='accepted_at_longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='arrived_at_latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='arrived_at_longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='drop_off_latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='drop_off_longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='pick_up_latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='pick_up_longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
    ]
