from django import forms
from .models import AirportRoute


class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = [
            'airport_code',
            'distance',
            'connected_airport',
            'position',
        ]


class SearchRouteForm(forms.Form):
    start_airport = forms.ModelChoiceField(
        queryset=AirportRoute.objects.all(),
        label="Start Airport"
    )
    direction = forms.ChoiceField(
        choices=[('L', 'Left'), ('R', 'Right')],
        label="Direction"
    )
