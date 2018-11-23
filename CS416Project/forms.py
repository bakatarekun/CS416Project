from django import forms

class TodoFrom(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder' : 'Enter to do here'}
    ))
    comment = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your comment here'}
    ))
