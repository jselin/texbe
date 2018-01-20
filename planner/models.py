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
    """All units in m unless otherwise stated"""
    name = models.CharField(max_length=200, 
        error_messages={'required': 'We really need you to fill in the name. Sory for bothering you'})

    finished_lenght = models.FloatField(
        help_text="Finished lenght of the weave in m")
    warp_shrinkage = models.IntegerField(default=8)
    warp_take_up = models.IntegerField(default=6)

    finished_width = models.FloatField()
    weft_shrinkage = models.IntegerField(default=8)
    weft_draw_in = models.IntegerField(default=6)

    picks_per_cm = models.FloatField()
    ends_per_cm = models.FloatField()

    test_lenght = models.FloatField(default=0)
    tying_lenght = models.FloatField(default=0.3)
    loom_waste_lenght = models.FloatField(default=0.6)
    fringe_lenght = models.FloatField(default=0)

    selvedge_width = models.FloatField(default=0)

    warp_yarn = models.ForeignKey(Yarn, on_delete=models.PROTECT, related_name='warp_yarn')
    weft_yarn = models.ForeignKey(Yarn, on_delete=models.PROTECT, related_name='weft_yarn')

    #calculated fields
    warp_lenght = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planner:plan_detail', kwargs={'pk': self.pk})

    @property
    def lenght(self):
        return finished_lenght + test_lenght
