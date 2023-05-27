from django import forms
from .models import ReservationPost

class ReservationModelForm(forms.ModelForm):

    class Meta:

        model = ReservationPost
        fields = ['user_name', 'user_phone', 'user_count', 'user_date', 'user_destination']