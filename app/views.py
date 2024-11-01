from django.shortcuts import render
from . import models

def index(request):
    banners = models.Banner.objects.last()
    about = models.About.objects.last()
    skills = models.Skill.objects.all()
    context = {
        'banner':banners,
        'about':about,
        'skills':skills
    }
    return render(request, 'index.html', context)