"""based on Boutique Ado walkthrough project"""

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        """links to Order model"""
        model = Order

        """sets specific fields to render"""
        fields = ('first_name', 'second_name', 'email', 
                  'phone_number', 'address1', 'address2',
                  'town_or_city', 'postcode', 'country',
                  'region_or_county',)


    def __init__(self, *args, **kwargs):
        """ calls and overrides init method """
        
        super().__init__(*args, **kwargs)

        """creates placeholders for form fields"""
        placeholders = {
            'first_name': 'First Name',
            'second_name': 'Second Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town / City',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'region_or_county': 'Region / County',
        }

        """uses autofocus to load page with cursor on first name field"""
        self.fields['first_name'].widget.attrs['autofocus'] = True

        """iterates through form fields"""
        for field in self.fields:
            """sets an asterisk in required fields"""
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            """gives placeholder attributes the values from the placeholders dictionary"""
            self.fields[field].widget.attrs['placeholder'] = placeholder
            """gives the form fields a CSS class"""
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            """removes existing labels from form fields"""
            self.fields[field].label = False