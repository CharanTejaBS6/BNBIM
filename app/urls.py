from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home,  name='home'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('update_tracker/', views.update_tracker, name='update_tracker'),
    path('order_tracker/', views.order_tracker, name='order_tracker'),
    path('crop-life-track-updates/', views.crop_life_track_updates, name='crop_life_track_updates'),
    path('edit_crop_life_tracker/<int:pk>/', views.edit_crop_life_tracker, name='edit_crop_life_tracker'),
    path('edit-cart-item/<int:item_id>/', views.edit_cart_item, name='edit_cart_item'),
    path('edit_wishlist_item/<int:item_id>/', views.edit_wishlist_item, name='edit_wishlist_item'),
    # path('crop-life-track-updates/', views.crop_life_track_updates,
    #      name='crop_life_track_updates'),
    # path('edit-crop-life-tracker/<int:crop_life_tracker_id>/',
    #      views.edit_crop_life_tracker, name='edit_crop_life_tracker'),
    # path('crop_life/', views.crop_life_tracker, name='crop_life_tracker'),
    # path('mark_completed/<int:stage_id>/', views.mark_stage_completed, name='mark_stage_completed'),
    # path('track/', views.track_plant, name='track_plant'),
    # path('trackp/', views.track_plant_details, name='track_plant'),
]
