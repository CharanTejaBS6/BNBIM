from django.contrib import admin
from app.models import CartItem, WishlistItem, CropLifeTracker

admin.site.register(CartItem)
admin.site.register(WishlistItem)
admin.site.register(CropLifeTracker)
