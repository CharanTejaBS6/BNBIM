from django import forms
from .models import CartItem, WishlistItem
from .models import CropLifeTracker


class CropLifeTrackerForm(forms.ModelForm):
    class Meta:
        model = CropLifeTracker
        fields = '__all__'


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['item_name', 'quantity']


class WishlistItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['item_name', 'item_price', 'quantity', 'date_added']
