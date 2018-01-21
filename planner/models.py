from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

class YarnManufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class YarnNumberingSystem(models.Model):
    name = models.CharField(max_length=3, unique=True)
    help = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Yarn(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(YarnManufacturer, on_delete=models.PROTECT)
    material = models.CharField(max_length=200)
    number = models.CharField(max_length=20,
        validators=[
        RegexValidator('(\d+([,.]?\d*)?){1}[ ]*([xX*/]{1}[ ]*\d*)?',
            message='Examples: "1.2" "5.3x2" "4,6/2"')])
    numbering_system = models.ForeignKey(YarnNumberingSystem, on_delete=models.PROTECT)
    sett = models.IntegerField()

    def get_absolute_url(self):
        return reverse('planner:yarn_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return ("%s, %s, %s, %s %s, %s yarns/cm" % (self.name, self.manufacturer, self.material, self.numbering_system, self.number, self.sett))

class Plan(models.Model):
    name = models.CharField(max_length=200, 
        error_messages={'required': 'We really need you to fill in the name. Sory for bothering you'})

        # Design
        finished_lenght_m = models.FloatField(
            help_text="Finished lenght of the weave in m")
        headings_hems_lenght_m = models.FloatField(default=0,
            verbose_name="some label",
            help_text="some help text")
        lenght_shrinkage_p = models.IntegerField(default=8)
        fringe_lenght_m = models.FloatField(default=0)

        finished_width_cm = models.FloatField()
        width_shrinkage_p = models.IntegerField(default=8)

        number_of_desigs = models.IntegerField(default=1)

        # Weawing
        test_piece_lenght_m = models.FloatField(default=0)
        number_of_test_pieces = models.IntegerField(default=1)
        loom_waste_lenght_m = models.FloatField(default=0.6)
        cutting_margin_m = models.FloatField(default=0.6)
        lenght_take_up_p = models.IntegerField(default=6)
        width_draw_in_p = models.IntegerField(default=6)
        selvedge_warps = models.IntegerField(default=2)

        # Yarns
        warp_yarn = models.ForeignKey(Yarn, on_delete=models.PROTECT, related_name='warp_yarn')
        weft_yarn = models.ForeignKey(Yarn, on_delete=models.PROTECT, related_name='weft_yarn')
        picks_per_cm = models.FloatField()
        ends_per_cm = models.FloatField()

        # On loom calculated
        warp_lenght_m = models.FloatField(null=True, blank=True)
        number_of_ends = models.IntegerField(null=True, blank=True)
        warp_width_cm = models.FloatField(null=True, blank=True)
        number_of_pics = models.IntegerField(null=True, blank=True)

        # Demand calculated
        warp_demand_g = models.FloatField(null=True, blank=True)
        weft_demand_g = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planner:plan_detail', kwargs={'pk': self.pk})
