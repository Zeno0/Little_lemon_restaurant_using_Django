from django import forms
from .models import Bookings

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['first_name', 'last_name', 'guest_num', 'comment', 'date' ,'phone']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # Render the date field as a date input
        }