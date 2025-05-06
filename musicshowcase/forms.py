from django import forms
import time

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=100, label="Subject", widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class': 'form-control'}))
    timestamp = forms.DateTimeField

    website = forms.CharField(
        required=False,
        label='Website',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'display:none;',  
            'tabindex': '-1',          
            'autocomplete': 'off'      
        })
    )
    timestamp = forms.FloatField(
        widget=forms.HiddenInput(),
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get('timestamp'):
            self.initial['timestamp'] = time.time()
    
    def clean(self):
        cleaned_data = super().clean()
        website = cleaned_data.get('website')
        timestamp = cleaned_data.get('timestamp')
        current_time = time.time()
        if website:
            raise forms.ValidationError("Form submission failed. Please try again.")
            
        if timestamp and (current_time - timestamp < 5):
                raise forms.ValidationError(
                    "Your form was submitted too quickly. Please try again."
                )
        
        return cleaned_data