from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CropLifeTracker(models.Model):
    plant_name = models.CharField(max_length=100)
    buy_seeds_or_saplings = models.BooleanField(default=False)
    preparation_of_soil_sowing = models.BooleanField(default=False)
    adding_manure_and_fertilizers = models.BooleanField(default=False)
    irrigation = models.BooleanField(default=False)
    harvesting_and_storage = models.BooleanField(default=False)

    def __str__(self):
        return self.plant_name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    # item_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    # date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.item_name


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.item_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class CropLifeTracker(models.Model):
    plant_name = models.CharField(max_length=100, default='Unknown')
    buy_seeds_or_saplings = models.BooleanField(default=False)
    preparation_of_soil_sowing = models.BooleanField(default=False)
    adding_manure_and_fertilizers = models.BooleanField(default=False)
    irrigation = models.BooleanField(default=False)
    harvesting_and_storage = models.BooleanField(default=False)


# class CartItem(models.Model):
#     item_name = models.CharField(max_length=100)
#     quantity = models.IntegerField(default=1)
#     # Add other fields as needed

#     def __str__(self):
#         return self.item_name



# class CropLifeTracker(models.Model):
#     stage_name = models.CharField(max_length=100)
#     completed = models.BooleanField(default=False)
#     skipped = models.BooleanField(default=False)


# class CropLifeStage(models.Model):
#     name = models.CharField(max_length=100)

# def create_default_stages(sender, **kwargs):
#     if kwargs['created_models']:
#         stages = [
#             "Buy Seeds or Saplings",
#             "Sowing",
#             "Ploughing",
#             "Irrigating",
#             "Harvesting"
#         ]
#         for stage in stages:
#             CropLifeStage.objects.create(name=stage)

# class CropLifeTracker(models.Model):
#     stage = models.ForeignKey(CropLifeStage, on_delete=models.CASCADE)
#     completed = models.BooleanField(default=False)

# # Create default stages when migrations are applied
# from django.db.models.signals import post_migrate
# post_migrate.connect(create_default_stages, sender=CropLifeStage)

# class CropLifeStage(models.Model):
#     name = models.CharField(max_length=100)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name


# class Plant(models.Model):
#     name = models.CharField(max_length=100)


# class TrackingStage(models.Model):
#     name = models.CharField(max_length=100)


# class TrackingEvent(models.Model):
#     plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
#     stage = models.ForeignKey(TrackingStage, on_delete=models.CASCADE)
#     expected_date = models.DateField()
#     completed = models.BooleanField(default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
