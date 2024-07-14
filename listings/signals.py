from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from cloudinary.uploader import destroy
from .models import MissingPerson

@receiver(post_delete, sender=MissingPerson)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        destroy(instance.image.public_id)

@receiver(pre_save, sender=MissingPerson)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_instance = MissingPerson.objects.get(pk=instance.pk)
    except MissingPerson.DoesNotExist:
        return False

    if old_instance.image and old_instance.image != instance.image:
        destroy(old_instance.image.public_id)
