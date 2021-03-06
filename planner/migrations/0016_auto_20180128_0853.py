# Generated by Django 2.0 on 2018-01-28 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0015_auto_20180127_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='number_of_desigs',
        ),
        migrations.AddField(
            model_name='plan',
            name='number_of_designs',
            field=models.IntegerField(default=1, verbose_name='Number of designs'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='cutting_margin_m',
            field=models.DecimalField(decimal_places=2, default=0.6, max_digits=4, verbose_name='Cutting margin'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='ends_per_cm',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='End per cm'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='finished_lenght_m',
            field=models.DecimalField(decimal_places=2, help_text='Finished lenght of the weave in m', max_digits=5, verbose_name='Finished lenght'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='finished_width_cm',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Finished width'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='fringe_lenght_m',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Fringe lenght'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='headings_hems_lenght_m',
            field=models.DecimalField(decimal_places=2, default=0, help_text='some help text', max_digits=4, verbose_name='Headings and hems'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='lenght_shrinkage_p',
            field=models.IntegerField(default=8, verbose_name='Lenght srinkage'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='lenght_take_up_p',
            field=models.IntegerField(default=6, verbose_name='Lenght take-up'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='loom_waste_lenght_m',
            field=models.DecimalField(decimal_places=2, default=0.6, max_digits=4, verbose_name='Loom waste'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='number_of_ends',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of ends'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='number_of_pics',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of pics'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='number_of_test_pieces',
            field=models.IntegerField(default=1, verbose_name='Number of test pieces'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='picks_per_cm',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Pics per cm'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='selvedge_warps',
            field=models.IntegerField(default=2, verbose_name='Selvedge warps'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='test_piece_lenght_m',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Test piece lenght'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='warp_demand_g',
            field=models.IntegerField(blank=True, null=True, verbose_name='Warp demand'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='warp_lenght_m',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Warp lenght'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='warp_width_cm',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, verbose_name='Warp width'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='warp_yarn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='warp_yarn', to='planner.Yarn', verbose_name='Warp yarn'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='weft_demand_g',
            field=models.IntegerField(blank=True, null=True, verbose_name='Weft demand'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='weft_yarn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='weft_yarn', to='planner.Yarn', verbose_name='Weft yarn'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='width_draw_in_p',
            field=models.IntegerField(default=6, verbose_name='Width draw-in'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='width_shrinkage_p',
            field=models.IntegerField(default=8, verbose_name='Width shrinkage'),
        ),
    ]
