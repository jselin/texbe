from django.forms import ModelForm
from .models import Plan    

class PlanForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['warp_lenght'].widget.attrs['readonly'] = True
        #self.initial['warp_lenght'] = instance.finished_lenght + instance.test_lenght
    class Meta:
        model = Plan
        fields = '__all__'