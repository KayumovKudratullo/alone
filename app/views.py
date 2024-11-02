from django.shortcuts import render
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from . import models


def index(request):
    banners = models.Banner.objects.last()
    about = models.About.objects.last()
    skills = models.Skill.objects.all()
    social_media = models.SocialMedia.objects.all()

    # recent work
    recent_works = models.RecentWork.objects.all()
    recent_works_with_hits = []
    for recent_work in recent_works:
        hit_count = HitCount.objects.get_for_object(recent_work)
        HitCountMixin.hit_count(request, hit_count)
        recent_works_with_hits.append({
            'recent_work': recent_work,
            'hit_count': hit_count.hits,
        })

    context = {
        'banner':banners,
        'about':about,
        'skills':skills,
        'recent_works_with_hits': recent_works_with_hits,
        'social_media':social_media,
    }
    return render(request, 'index.html', context)
