from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

HEIGHT = 64
WIDTH = 64


class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    avatar = models.URLField(blank=True)


class Scan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ct_scan = models.ImageField(upload_to='ct_scans', blank=True)
    cancer = models.FloatField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        im = Image.open(self.ct_scan)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((HEIGHT, WIDTH))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.ct_scan = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.ct_scan.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Scan, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


