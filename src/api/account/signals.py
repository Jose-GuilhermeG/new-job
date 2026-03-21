from account.models import Profile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

USER = get_user_model()

@receiver(signal=post_save , sender=USER)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance , name = instance.username)
