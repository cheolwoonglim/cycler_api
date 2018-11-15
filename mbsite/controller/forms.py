from django.forms import ModelForm

from controller.models import Cyclers, CyclerInput

class CyclersForm(ModelForm):
    class Meta:
        model = Cyclers
        fields = ['name', 'url', 'x', 'y']

class CyclerInputForm(ModelForm):
    class Meta:
        model = CyclerInput
        fields = ['node', 'status', 'wafer', 'array', 'Tstart',
                  'Icharge', 'Idischarge', 'Vmax', 'Vmin', 'Tstep', 'schedule']
