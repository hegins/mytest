from django import forms
from .models import serverlist

class ServerListForm(forms.ModelForm):

    class Meta:
        model = serverlist
        fields = ('ip', 'Cmac', 'Cname', 'user', 'position', 'server', 'OS')
        widgets = {
          'ip': forms.TextInput(attrs={'class': 'form-control'}),
          'Cmac': forms.TextInput(attrs={'class': 'form-control'}),
          'Cname': forms.TextInput(attrs={'class': 'form-control'}),
          'user': forms.TextInput(attrs={'class': 'form-control'}),
          'position': forms.TextInput(attrs={'class': 'form-control'}),
          'server': forms.TextInput(attrs={'class': 'form-control'}),
          'OS': forms.TextInput(attrs={'class': 'form-control'}),
        }
