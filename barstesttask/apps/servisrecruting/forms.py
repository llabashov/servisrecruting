from django import forms
from .models import Recrut
from django.core.exceptions import ValidationError


class RecrutForm(forms.Form):
    recrut_name = forms.CharField(max_length=50)
    recrut_planet = forms.CharField(max_length = 50)
    recrut_age= forms.CharField(max_length = 50)
    recrut_email = forms.EmailField(max_length = 254)

    def clean_recrut(self):
        new_recrut = self.cleaned_data['recrut_name'].lower()

        if new_recrut == 'create_recrut':
            raise ValidationError('Име не может быть "create_recrut"')
        return new_recrut

    def save(self):
        new_recrut = Recrut.objects.create(
            recrut_name=self.cleaned_data['recrut_name'],
            recrut_planet=self.cleaned_data['recrut_planet'],
            recrut_age=self.cleaned_data['recrut_age'],
            recrut_email=self.cleaned_data['recrut_email'],
        )
        return new_recrut