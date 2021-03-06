from django.forms import ModelForm
from .models import Plan    

class PlanForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        #instance = getattr(self, 'instance', None)
        #if instance and instance.pk:
        self.fields['warp_lenght_m'].widget.attrs['readonly'] = True
        self.fields['number_of_ends'].widget.attrs['readonly'] = True
        self.fields['warp_width_cm'].widget.attrs['readonly'] = True
        self.fields['number_of_pics'].widget.attrs['readonly'] = True
        self.fields['warp_demand_g'].widget.attrs['readonly'] = True
        self.fields['weft_demand_g'].widget.attrs['readonly'] = True

        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({'class':'has-popover', 'data-content':help_text, 'data-placement':'right', 'data-container':'body'})

    class Meta:
        model = Plan
        fields = '__all__'
