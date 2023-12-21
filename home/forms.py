from django import forms 
from .models import Todo

class TodoCreatForm(forms.Form):
    title = forms.CharField(label="subject", required=False)
    body = forms.CharField()
    created = forms.DateTimeField()  


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('__all__')