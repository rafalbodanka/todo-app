from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title',]
        labels = {
            'title': ''
        }
        required = ()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form',
                'placeholder': 'Task'}),
        }
    # title = forms.CharField(label='',
    # max_length=30,
    # required=False,
    # widget=forms.TextInput(attrs={'class': 'form', 'placeholder': 'Task', 'required': 'True'}))
