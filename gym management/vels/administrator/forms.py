from django import forms
from .models import Member

class HotelForm(forms.ModelForm):
  
    class Meta:
        model = Member
        fields = ['name', 'Member_image']