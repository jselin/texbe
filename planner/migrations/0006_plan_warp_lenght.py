# Generated by Django 2.0 on 2018-01-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20180109_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='warp_lenght',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]