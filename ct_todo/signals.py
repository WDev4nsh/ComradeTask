from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kawrgs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Only save profile when profile exist
        try:
            instance.userprofile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
