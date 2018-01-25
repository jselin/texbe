from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
import re
from decimal import *

class YarnManufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Yarn(models.Model):
    YARN_NUMBERING_SYSTEM = (
        ('TEX', 'TEX'),
        ('NEP', 'NEP'),
        ('NE', 'NE'),
        ('NM', 'NM'),
        ('DEN', 'DEN'),
    )

    #number_regexp = '(\d+([,.]?\d*)?){1}[ ]*([xX*/]{1}[ ]*\d*)?'
    NUMBER_VALIDATOR = '(\d+[,.]?\d*){1}[ ]*(?:([xX*/]{1})[ ]*(\d+))?'
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(
        YarnManufacturer, on_delete=models.PROTECT)
    material = models.CharField(max_length=200)
    number = models.CharField(max_length=20,
                              validators=[
                                RegexValidator(NUMBER_VALIDATOR,
                                message='Examples: "1.2" "5.3x2" "4,6/2"')])
    numbering_system = models.CharField(max_length=3, choices=YARN_NUMBERING_SYSTEM)
    sett = models.IntegerField()

    def get_absolute_url(self):
        return reverse('planner:yarn_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return ("%s, %s, %s, %s %s, %s yarns/cm" % (self.name, self.manufacturer, self.material, self.numbering_system, self.number, self.sett))

    @property
    def tex_number(self):
        p = re.compile(self.NUMBER_VALIDATOR)
        sub = p.findall(self.number)
        v = Decimal(sub[0][0])
        if sub[0][2] is None or len(sub[0][2]) is 0:
            n = Decimal(1)
        else:
            n = Decimal(sub[0][2])
        if(self.numbering_system == 'TEX'):
            return v * n
        elif(self.numbering_system == 'NEP'):
            pass
        elif(self.numbering_system == 'NE'):
            pass
        elif(self.numbering_system == 'NM'):
            pass
        elif(self.numbering_system == 'DEN'):
            pass
        else:
            print("Something went haywire")
            return 0


class Plan(models.Model):
    name = models.CharField(max_length=200,
                            error_messages={'required': 'We really need you to fill in the name. Sory for bothering you'})

    # Design
    finished_lenght_m = models.DecimalField(max_digits=5, decimal_places=2,
        help_text="Finished lenght of the weave in m")
    headings_hems_lenght_m = models.DecimalField(max_digits=4, decimal_places=2, default=0,
                                                verbose_name="Heading and hems",
                                                help_text="some help text")
    lenght_shrinkage_p = models.IntegerField(default=8)
    fringe_lenght_m = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    finished_width_cm = models.DecimalField(max_digits=5, decimal_places=1)
    width_shrinkage_p = models.IntegerField(default=8)

    number_of_desigs = models.IntegerField(default=1)

    # Weawing
    test_piece_lenght_m = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    number_of_test_pieces = models.IntegerField(default=1)
    loom_waste_lenght_m = models.DecimalField(max_digits=4, decimal_places=2, default=0.6)
    cutting_margin_m = models.DecimalField(max_digits=4, decimal_places=2, default=0.6)
    lenght_take_up_p = models.IntegerField(default=6)
    width_draw_in_p = models.IntegerField(default=6)
    selvedge_warps = models.IntegerField(default=2)

    # Yarns
    warp_yarn = models.ForeignKey(
        Yarn, on_delete=models.PROTECT, related_name='warp_yarn')
    weft_yarn = models.ForeignKey(
        Yarn, on_delete=models.PROTECT, related_name='weft_yarn')
    picks_per_cm = models.DecimalField(max_digits=4, decimal_places=1)
    ends_per_cm = models.DecimalField(max_digits=4, decimal_places=1)

    # On loom calculated
    warp_lenght_m = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, )
    number_of_ends = models.IntegerField(null=True, blank=True)
    warp_width_cm = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    number_of_pics = models.IntegerField(null=True, blank=True)

    # Demand calculated
    warp_demand_g = models.IntegerField(null=True, blank=True)
    weft_demand_g = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planner:plan_detail', kwargs={'pk': self.pk})
