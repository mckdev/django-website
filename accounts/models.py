from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Profile(models.Model):
    """
    Define model for user profile with one-to-one relationship with User table.
    """
    class Meta:
        verbose_name_plural = "User profiles"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    country = CountryField(blank=True)
    about = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username


# Define signals to update user profile whenever we create/update User model.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create Profile object whenever new User object is created.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Update Profile object whenever new User object is updated.
    """
    instance.profile.save()
