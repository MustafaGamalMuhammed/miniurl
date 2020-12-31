from url_shortener.models import ShorteneddURL
from django import forms


class ShorteneddURLForm(forms.ModelForm):
    class Meta:
        model = ShorteneddURL
        fields = ["url"]
