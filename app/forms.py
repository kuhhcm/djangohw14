from django import forms

class CreateTodoForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.CharField(max_length=20)
    