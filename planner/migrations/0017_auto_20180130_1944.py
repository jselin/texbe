# Generated by Django 2.0 on 2018-01-30 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0016_auto_20180128_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(error_messages={'required': 'We really need you to fill in the name'}, max_length=200),
        ),
    ]