from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from cloudinary import uploader
from .models import MissingPerson

@receiver(post_delete, sender=MissingPerson)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.photo:
        uploader.destroy(instance.photo.name)

@receiver(pre_save, sender=MissingPerson)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_instance = MissingPerson.objects.get(pk=instance.pk)
    except MissingPerson.DoesNotExist:
        return False

    if old_instance.photo and old_instance.photo != instance.photo:
        uploader.destroy(old_instance.photo.name)