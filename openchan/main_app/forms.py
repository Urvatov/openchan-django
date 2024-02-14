from django import forms
from main_app.models import Thread


class AddThread(forms.Form):
    title = forms.CharField(max_length=256)
    text = forms.Textarea()