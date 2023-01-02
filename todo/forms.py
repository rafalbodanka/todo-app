from django import forms

class Task(forms.Form):
    title = forms.CharField(label='',
    max_length=30,
    widget=forms.TextInput(attrs={'class': 'form', 'placeholder': 'Task'}))
    # description = forms.CharField(label='description', max_length=100)