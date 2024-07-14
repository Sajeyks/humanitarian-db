from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from cloudinary.models import CloudinaryField

# class FallenSoldier(models.Model):
#     name = models.CharField(max_length=100)
#     reason_of_death = models.TextField()
#     place_killed = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     date = models.DateField()
#     photo = models.ImageField(upload_to='fallen_soldiers/', null=True, blank=True)
    
#     def image_tag(self):
#         return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.photo))

#     def __str__(self):
#         return self.name

# class ArrestedPerson(models.Model):
#     name = models.CharField(max_length=100)
#     police_station = models.CharField(max_length=100)
#     has_representation = models.BooleanField(default=False)
#     date = models.DateField()
#     photo = models.ImageField(upload_to='media/arrested_people/', null=True, blank=True)
    
#     def image_tag(self):
#         return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.photo))


#     def __str__(self):
#         return self.name

class MissingPerson(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, unique=True)
    time_of_missing = models.DateTimeField()
    found = models.BooleanField(default=False)
    date_found = models.DateField(null=True, blank=True)
    photo =ProcessedImageField(upload_to='avatars',
                                 processors=[ResizeToFill(400, 400)],
                                 format='JPEG',
                                 options={'quality': 90},
                                 blank=True,
                                 null=True)

    # def image_tag(self):
    #     return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.photo))

    def __str__(self):
        return self.name