from django import forms

class TextInputForm(forms.Form):
    input_text = forms.CharField(label='Input Text', max_length=100)
