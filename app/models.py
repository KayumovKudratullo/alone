from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from app.translationn import translating


class Banner(models.Model):
    # title = models.CharField(max_length=255)
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
    

class Education(models.Model):
    # title = models.CharField(max_length=150)
    title_eng = models.CharField(max_length=150)
    title_ru = models.CharField(blank=True, max_length=150)
    title_uz = models.CharField(blank=True, max_length=150)
    title_de = models.CharField(blank=True, max_length=150)
    # text = models.TextField()
    name_eng = models.TextField()
    name_ru = models.TextField(blank=True)
    name_uz = models.TextField(blank=True)
    name_de = models.TextField(blank=True)
    
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


class WorkExperiance(models.Model):
    # work_place = models.CharField(max_length=255)
    work_place_eng = models.CharField(max_length=255)
    work_place_ru = models.CharField(blank=True, max_length=255)
    work_place_uz = models.CharField(blank=True, max_length=255)
    work_place_de = models.CharField(blank=True, max_length=255)
    # text = models.TextField()
    text_eng = models.TextField()
    text_ru = models.TextField(blank=True)
    text_uz = models.TextField(blank=True)
    text_de = models.TextField(blank=True)
    img = models.ImageField(upload_to='workPlace/')
    year_start = models.DateField()
    year_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.work_place_eng
    
    def save(self, *args, **kwargs):
        self.fill_out()
        super().save(*args, **kwargs)

    def fill_out(self):
        data = translating(self.work_place_eng)
        self.work_place_ru = data['ru']
        self.work_place_uz = data['uz']
        self.work_place_de = data['de']


class RecentWork(models.Model):
    img = models.ImageField(upload_to='recentWork/')
    # title = models.CharField(max_length=200)
    title_eng = models.CharField(max_length=200)
    title_ru = models.CharField(blank=True, max_length=200)
    title_uz = models.CharField(blank=True, max_length=200)
    title_de = models.CharField(blank=True, max_length=200)
    link = models.TextField()

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
    # name = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    name_ru = models.CharField(blank=True, max_length=255)
    name_uz = models.CharField(blank=True, max_length=255)
    name_de = models.CharField(blank=True, max_length=255)
    number = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    # message = models.TextField()
    message_eng = models.TextField()
    message_ru = models.TextField(blank=True)
    message_uz = models.TextField(blank=True)
    message_de = models.TextField(blank=True)

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
    # name = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=50)
    name_ru = models.CharField(blank=True, max_length=50)
    name_uz = models.CharField(blank=True, max_length=50)
    name_de = models.CharField(blank=True, max_length=50)
    icon = models.ImageField(upload_to='Social Media/')
    link = models.TextField()

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