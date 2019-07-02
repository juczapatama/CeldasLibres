from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class Usuario(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='usuario', null=True
    )
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Usuario.objects.get_or_create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, *args, **kwargs):
    instance.usuario.save()