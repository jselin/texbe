from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
import re
from decimal import *
from django.contrib.auth.models import User


class YarnManufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Yarn(models.Model):
    YARN_NUMBERING_SYSTEM = (
        ('TEX', 'tex (g/1.000m)'), # Mass of yarn in grams per 1000m
        ('DTEX', 'dtex (g/10.000m)'), # Mass of yarn in grams per 10000m
        ('DEN', 'den (Denier, g/9.000m)'), # Mass of yarn in grams for leght of 9000,
        ('NM', 'Nm (Metric yarn number, m/g)'), # Lengh in meters per 1g of mass
        ('NE', 'Ne (English cotton yarn number) aka ECC'), # Number of 840 yard strands per 1 Englih pound of mass
        ('NEL', 'NeL (English linen yarn number)'), # Number of 300 yard strands per 1 Englih pound of mass
        ('NEK', 'NeK (English wool yarn number, worsted)'), # Number of 300 yard strands per 1 Englih pound of mass
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
    numbering_system = models.CharField(max_length=4, choices=YARN_NUMBERING_SYSTEM)
    sett = models.IntegerField()

    def get_absolute_url(self):
        return reverse('planner:yarn_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return ("%s, %s, %s, %s %s, %s yarns/cm" % (self.name, self.manufacturer, self.material, self.numbering_system, self.number, self.sett))

    @property
    def tex_number(self):
        """http://www.swicofil.com/companyinfo/manualyarnnumbering.html"""
        p = re.compile(self.NUMBER_VALIDATOR)
        sub = p.findall(self.number)
        v = Decimal(sub[0][0].replace(',','.'))
        if sub[0][2] is None or len(sub[0][2]) is 0:
            n = 1
        else:
            n = Decimal(sub[0][2])
        
        if(self.numbering_system == 'TEX'):
            return (v * n)
        elif(self.numbering_system == 'DTEX'):
            return (v * n) / Decimal(10)
        elif(self.numbering_system == 'DEN'):
            return  (v * n) / Decimal(9)
        elif(self.numbering_system == 'NEL'):
            return Decimal(1653.515493) / (v / n)
        elif(self.numbering_system == 'NE'):
            return Decimal(590.5412474) / (v / n)
        elif(self.numbering_system == 'NEK'):
            return Decimal(885.8118712) / (v / n)
        elif(self.numbering_system == 'NM'):
            return Decimal(1000) / (v / n)
        else:
            print("Something went haywire")
            return 0


class Plan(models.Model):
    created_by = models.ForeignKey(User, editable=False, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=200,
                            error_messages={'required': 'We really need you to fill in the name'})

    public = models.BooleanField(default=True, verbose_name="Public")

    # Design
    finished_lenght_m = models.DecimalField(max_digits=5, decimal_places=2,
                                        verbose_name="Finished lenght",
                                        help_text="Lenght of finished fabric for one design")
    headings_hems_lenght_m = models.DecimalField(max_digits=4, decimal_places=2, default=0,
                                        verbose_name="Headings and hems",
                                        help_text="Lenght of headings and hems for one design")
    lenght_shrinkage_p = models.IntegerField(default=8,
                                        verbose_name="Lenght shrinkage",
                                        help_text="Expected shrinkage in lenght of the woven fabric for one design")
    fringe_lenght_m = models.DecimalField(max_digits=4, decimal_places=2, default=0,
                                        verbose_name="Fringe lenght",
                                        help_text="Lenght of fringes for one design")

    finished_width_cm = models.DecimalField(max_digits=5, decimal_places=1,
                                        verbose_name="Finished width",
                                        help_text="Width of finished fabric for one design")
    width_shrinkage_p = models.IntegerField(default=8,
                                        verbose_name="Width shrinkage",
                                        help_text="Expected shinkage in width of the woven fabric for one design")

    number_of_designs = models.IntegerField(default=1,
                                        verbose_name="Number of designs",
                                        help_text="Number of designs to be woven")

    # Weawing
    test_piece_lenght_m = models.DecimalField(max_digits=4, decimal_places=2, default=0,
                                        verbose_name="Sample lenght",
                                        help_text="Lenght reserved for weaving a sample")
    number_of_test_pieces = models.IntegerField(default=1,
                                        verbose_name="Number of samples",
                                        help_text="Number of samples to be woven")
    loom_waste_lenght_m = models.DecimalField(max_digits=4, decimal_places=2, default=0.6,
                                        verbose_name="Loom waste",
                                        help_text="Lenght needed for tying the warp on the loom, and, lenght needed at the end. Add about 70 cm for table loom, or 90 cm for a floor loom. Minimum warp length reserved for tying the warp is 0,15 m and at the end 0,35 m when amount of shafts is 2-4. For every additional shaft 0,05 m must be added.")
    cutting_margin_m = models.DecimalField(max_digits=4, decimal_places=2, default=0.6,
                                        verbose_name="Cutting margin",
                                        help_text="Lenght between the designs or samples reserved for cutting them separate")
    lenght_take_up_p = models.IntegerField(default=6,
                                        verbose_name="Lenght take-up",
                                        help_text="Expected take-up due to interlacement")
    width_draw_in_p = models.IntegerField(default=6,
                                        verbose_name="Width draw-in",
                                        help_text="Expected width draw-in due to interlacement")
    selvedge_warps = models.IntegerField(default=2,
                                        verbose_name="Selvedge warps",
                                        help_text="Total number of additional warp ends for the selvedges")

    # Yarns
    warp_yarn = models.ForeignKey(
        Yarn, on_delete=models.PROTECT, related_name='warp_yarn',
                                        verbose_name="Warp yarn",
                                        help_text="Yarn used for warp")
    weft_yarn = models.ForeignKey(
        Yarn, on_delete=models.PROTECT, related_name='weft_yarn',
                                        verbose_name="Weft yarn",
                                        help_text="Yarn used for weft")
    picks_per_cm = models.DecimalField(max_digits=4, decimal_places=1,
                                        verbose_name="Pics per cm",
                                        help_text="Number of weft yarn layers per cm")
    ends_per_cm = models.DecimalField(max_digits=4, decimal_places=1,
                                        verbose_name="Ends per cm",
                                        help_text="Number of warp yarns per cm")

    # On loom calculated
    warp_lenght_m = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True,
                                        verbose_name="Warp lenght")
    number_of_ends = models.IntegerField(null=True, blank=True,
                                        verbose_name="Number of ends")
    warp_width_cm = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True,
                                        verbose_name="Warp width")
    number_of_pics = models.IntegerField(null=True, blank=True,
                                        verbose_name="Number of pics")

    # Demand calculated
    warp_demand_g = models.IntegerField(null=True, blank=True,
                                        verbose_name="Warp demand")
    weft_demand_g = models.IntegerField(null=True, blank=True,
                                        verbose_name="Weft demand")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planner:plan_detail', kwargs={'pk': self.pk})

    def get_verbose_name(self):
        return self._meta.verbose_name
