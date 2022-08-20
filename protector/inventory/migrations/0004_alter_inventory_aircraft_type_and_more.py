# Generated by Django 4.1 on 2022-08-20 12:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventory_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='aircraft_type',
            field=models.ManyToManyField(null=True, to='inventory.aircrafttype'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='alternative_part_number',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='descriptions',
            field=models.TextField(null=True),
        ),
    ]
