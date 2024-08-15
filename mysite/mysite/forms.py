from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your name . . .", "size": "40"}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "YourEmail@example.com", "size": "40"}),
        validators=[EmailValidator],
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject", "size": "40"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message . . .", "cols": "43", "rows": "10"})
    )