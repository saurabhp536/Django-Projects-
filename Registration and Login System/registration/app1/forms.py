from django import forms
from .models import UserProfile
from .models import Contact 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'mobile_number', 'address', 'date_of_birth']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Specify the model to use for this form
        fields = ['name', 'email', 'subject', 'message']  # Specify which fields to include in the form
