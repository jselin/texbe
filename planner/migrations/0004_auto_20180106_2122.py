# Generated by Django 2.0 on 2018-01-06 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_auto_20180106_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('finished_lenght', models.FloatField()),
                ('warp_shrinkage', models.IntegerField(default=8)),
                ('warp_take_up', models.IntegerField(default=6)),
                ('finished_width', models.FloatField()),
                ('weft_shrinkage', models.IntegerField(default=8)),
                ('weft_draw_in', models.IntegerField(default=6)),
                ('picks_per_cm', models.FloatField()),
                ('ends_per_cm', models.FloatField()),
                ('test_lenght', models.FloatField(default=0)),
                ('tying_lenght', models.FloatField(default=0.3)),
                ('loom_waste_lenght', models.FloatField(default=0.6)),
                ('fringe_lenght', models.FloatField(default=0)),
                ('selvedge_width', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='yarn',
            name='sett_unit',
        ),
        migrations.AddField(
            model_name='plan',
            name='warp_yarn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='warp_yarn', to='planner.Yarn'),
        ),
        migrations.AddField(
            model_name='plan',
            name='weft_yarn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='weft_yarn', to='planner.Yarn'),
        ),
    ]