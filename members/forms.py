from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone', 'email', 'plan', 'fee_status', 'trainer', 'applied_offer', 'is_active']
        widgets = {
            'phone': forms.TextInput(attrs={'maxlength': '10', 'placeholder': '10 digit mobile number'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number mein sirf numbers (0-9) hone chahiye.")
        if len(phone) != 10:
            raise forms.ValidationError("Phone number bilkul 10 digits ka hona chahiye.")
        return phone
    
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone', 'email', 'plan', 'fee_status', 'trainer', 'is_active']
        widgets = {
            'phone': forms.TextInput(attrs={'maxlength': '10', 'placeholder': '10 digit mobile number'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number mein sirf numbers (0-9) hone chahiye.")
        if len(phone) != 10:
            raise forms.ValidationError("Phone number bilkul 10 digits ka hona chahiye.")
        return phone

