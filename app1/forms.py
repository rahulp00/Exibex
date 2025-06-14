from django import forms

class PaintingForm(forms.Form):
    prompt = forms.CharField(label='Describe your painting', max_length=200)
