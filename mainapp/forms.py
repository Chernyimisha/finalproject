from django import forms
from .models import APIKey, APIUrl


class APIKeyForm(forms.ModelForm):
    class Meta:
        model = APIKey
        fields = [
            'company', 'description', 'key',
        ]


class APIUrlForm(forms.ModelForm):
    class Meta:
        model = APIUrl
        fields = [
            'description', 'url', 'request', 'validity',
        ]
