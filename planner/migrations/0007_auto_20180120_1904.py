# Generated by Django 2.0 on 2018-01-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_plan_warp_lenght'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='warp_lenght',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
