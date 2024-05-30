from django import forms
from .models import Item, Rating, Prescription, Coupon

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }



class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']
        

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient_name','prescription_images','prescription_pdf', 'message']


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['coupon_name', 'coupon_code', 'coupon_value', 'coupon_description','valid_from','valid_to','usage_limit','usage_count', 'applicable_products','min_purchase_amount']  # Add other fields as needed
        labels = {
            'coupon_name': 'Coupon Name',
            'coupon_code': 'Coupon Code',
            'coupon_value': 'Coupon Value', 
            'coupon_description': 'coupon_description',
            'valid_from':'valid_from',
            'valid_to': 'valid_to',
            'usage_limit':'usage_limit',
            'usage_count':'usage_count',
            'applicable_products':'applicable_products',
            'min_purchase_amount':'min_purchase_amount',
           
        }
        
    