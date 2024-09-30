from django import forms
from .models import Schedule, Stop

class ScheduleForm(forms.ModelForm):
    stops = forms.ModelMultipleChoiceField(
        queryset=Stop.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Оберіть зупинки'
    )
     
    class Meta:
        model = Schedule
        fields = ['route', 'departure_time', 'arrival_time', 'stops']
