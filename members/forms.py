from django import forms
from .models import ContactMessage, Member

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'required': 'True'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address', 'required': 'True'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number (10 digits)', 'maxlength': '10', 'required': 'True'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message or Inquiry...', 'required': 'True'}),
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone', 'email', 'plan', 'fee_status', 'trainer', 'applied_offer', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit Phone', 'maxlength': '10'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'plan': forms.Select(attrs={'class': 'form-control'}),
            'fee_status': forms.Select(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'applied_offer': forms.Select(attrs={'class': 'form-control'}),
        }