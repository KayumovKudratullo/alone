from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from app.translationn import translating
from hitcount.models import HitCount
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

        
class Banner(models.Model):
    title_eng = models.CharField(max_length=255)
    title_ru = models.CharField(blank=True, max_length=255)
    title_uz = models.CharField(blank=True, max_length=255)
    title_de = models.CharField(blank=True, max_length=255)
    img = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title_eng
    
    def save(self, *args, **kwargs):
        self.fill_out()
        super().save(*args, **kwargs)

    def fill_out(self):
        data = translating(self.title_eng)
        self.title_ru = data['ru']
        self.title_uz = data['uz']
        self.title_de = data['de']

    

class About(models.Model):
    text = RichTextUploadingField()

    def __str__(self):
        return self.text


class Skill(models.Model):
    # name = models.CharField(max_length=150)
    name_eng = models.CharField(max_length=150)
    name_ru = models.CharField(blank=True, max_length=150)
    name_uz = models.CharField(blank=True, max_length=150)
    name_de = models.CharField(blank=True, max_length=150)
    icon = models.ImageField(upload_to='icon/')

    def __str__(self):
        return self.name_eng
    
    def save(self, *args, **kwargs):
        self.fill_out()
        super().save(*args, **kwargs)

    def fill_out(self):
        data = translating(self.name_eng)
        self.name_ru = data['ru']
        self.name_uz = data['uz']
        self.name_de = data['de']
    

class RecentWork(models.Model):
    img = models.ImageField(upload_to='recentWork/')
    title_eng = models.CharField(max_length=200)
    title_ru = models.CharField(blank=True, max_length=200)
    title_uz = models.CharField(blank=True, max_length=200)
    title_de = models.CharField(blank=True, max_length=200)
    link = models.TextField()
    # Use the HitCountMixin to enable tracking
    hit_count_generic = models.ForeignKey(HitCount, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title_eng
    
    def save(self, *args, **kwargs):
        self.fill_out()
        super().save(*args, **kwargs)

    def fill_out(self):
        data = translating(self.title_eng)
        self.title_ru = data['ru']
        self.title_uz = data['uz']
        self.title_de = data['de']


class Contact(models.Model):
    # address = models.TextField()
    address_eng = models.TextField()
    address_ru = models.TextField(blank=True)
    address_uz = models.TextField(blank=True)
    address_de = models.TextField(blank=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.email #save va fill_out qoyilmadi
    

class CommentForm(models.Model):
    name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    # name = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    name_ru = models.CharField(blank=True, max_length=100)
    name_uz = models.CharField(blank=True, max_length=100)
    name_de = models.CharField(blank=True, max_length=100)
    # about = models.CharField(max_length=255)
    about_eng = models.CharField(max_length=255)
    about_ru = models.CharField(blank=True, max_length=255)
    about_uz = models.CharField(blank=True, max_length=255)
    about_de = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name_eng
    
    def save(self, *args, **kwargs):
        self.fill_out()
        super().save(*args, **kwargs)

    def fill_out(self):
        data = translating(self.name_eng)
        self.name_ru = data['ru']
        self.name_uz = data['uz']
        self.name_de = data['de']


class SocialMedia(models.Model):
    icon = models.CharField(max_length=60)
    link = models.TextField()

    def __str__(self):
        return self.icon
    

import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models

@receiver(post_delete)
def delete_image_file(sender, instance, **kwargs):
    # Loop through all fields of the instance
    for field in instance._meta.fields:
        # Check if the field is an ImageField or FileField
        if isinstance(field, (models.ImageField, models.FileField)):
            file_field = getattr(instance, field.name)
            # Delete the file if it exists
            if file_field and os.path.isfile(file_field.path):
                os.remove(file_field.path)
