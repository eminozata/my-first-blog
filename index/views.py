from django.shortcuts import render
from .models import ArchivePost
from django.utils import timezone



# Create your views here.
def index(request):
    posts = ArchivePost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    context = {'posts':posts}
    return render(request, 'index/index.html', context)

def archive(request):
    
    posts = ArchivePost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index/archive.html', {'posts': posts})

def about(request):
    return render(request, 'index/about.html', {})