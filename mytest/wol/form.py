from django import forms

class addHostForm(forms.Form):
    ip=forms.CharField(label='ip',max_length=20)
