from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CartItem
from .forms import CartItemForm
from .models import WishlistItem
from .forms import WishlistItemForm
from .models import CropLifeTracker
from .forms import CropLifeTrackerForm


def edit_wishlist_item(request, item_id):
    # Retrieve the wishlist item based on its ID
    item = WishlistItem.objects.get(id=item_id)

    if request.method == 'POST':
        # Populate the form with the POST data and instance of the item
        form = WishlistItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Redirect to the wishlist page after saving
            return redirect('wishlist')
    else:
        # Populate the form with the instance of the item
        form = WishlistItemForm(instance=item)

    return render(request, 'edit_wishlist_item.html', {'form': form})


def edit_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('cart')
    else:
        form = CartItemForm(instance=item)
    return render(request, 'edit_cart_item.html', {'form': form})


def crop_life_track_updates(request):
    crop_life_trackers = CropLifeTracker.objects.all()
    return render(request, 'crop_life_track_updates.html', {'crop_life_trackers': crop_life_trackers})


def edit_crop_life_tracker(request, pk):
    crop_life_tracker = get_object_or_404(CropLifeTracker, pk=pk)
    if request.method == 'POST':
        form = CropLifeTrackerForm(request.POST, instance=crop_life_tracker)
        if form.is_valid():
            form.save()
            # Redirect back to the main page after saving
            return redirect('crop_life_track_updates')
    else:
        form = CropLifeTrackerForm(instance=crop_life_tracker)
    return render(request, 'edit_crop_life_tracker.html', {'form': form})


def order_tracker(request):
    if request.method == 'POST':
        form = CropLifeTrackerForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the same page after saving
            return redirect('order_tracker')
    else:
        form = CropLifeTrackerForm()

    return render(request, 'crop_life_tracker.html', {'form': form})


# def crop_life_track_updates(request):
#     crop_life_trackers = CropLifeTracker.objects.all()
#     return render(request, 'crop_life_track_updates.html', {'crop_life_trackers': crop_life_trackers})

# def update_tracker(request):
#     return render(request, 'crop_life_tracker.html')


# def update_tracker(request):
#     if request.method == 'POST':
#         data = request.POST
#         stage_name = data.get('stage_name')
#         completed = data.get('completed', False)
#         skipped = data.get('skipped', False)

#         tracker, created = CropLifeTracker.objects.get_or_create(stage_name=stage_name)
#         tracker.completed = completed
#         tracker.skipped = skipped
#         tracker.save()

#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request method'})
# def crop_life_tracker(request):
#     if request.method == 'POST':
#         stage_ids = request.POST.getlist('stage_ids')
#         for stage_id in stage_ids:
#             stage = CropLifeStage.objects.get(pk=stage_id)
#             stage.completed = True
#             stage.save()
#         return redirect('crop_life_tracker')

#     stages = CropLifeStage.objects.all()
#     return render(request, 'crop_life_tracker.html', {'stages': stages})

# def mark_stage_completed(request, stage_id):
#     stage = CropStage.objects.get(pk=stage_id)
#     stage.completed = True
#     stage.save()
#     return redirect('crop_life_tracker')

# def track_plant(request):
#     if request.method == 'POST':
#         form = PlantForm(request.POST)
#         if form.is_valid():
#             plant = form.save()
#             # return render(request, 'track_plant.html')
#             return redirect('tracking', plant_id=plant.id)
#     else:
#         form = PlantForm()
#     return render(request, 'track_plant.html', {'form': form})


# def track_plant_details(request, plant_id):
#     plant = Plant.objects.get(pk=plant_id)
#     stages = TrackingStage.objects.all()
#     events = TrackingEvent.objects.filter(plant=plant)
#     if request.method == 'POST':
#         form = TrackingEventForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.plant = plant
#             event.user = request.user
#             event.save()
#             return redirect('tracking_details', plant_id=plant.id)
#     else:
#         form = TrackingEventForm()
#     return render(request, 'track_plant_details.html', {'plant': plant, 'stages': stages, 'events': events, 'form': form})


def home(request):
    return render(request, 'home.html')


def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


def add_to_wishlist(request):
    if request.method == 'POST':
        form = WishlistItemForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.save()
    return redirect('wishlist')


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})


def add_to_cart(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.user = request.user
            cart_item.save()
    return redirect('cart')


def index(request):
    return render(request, 'welcome.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Redirect to the home page after successful login
            return render(request, 'home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')
