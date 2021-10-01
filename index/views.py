from django.shortcuts import render
from .models import ArchivePost
from .forms import ContactForm
from django.utils import timezone



# Create your views here.
def index(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index/index.html')
    form = ContactForm()
    posts = ArchivePost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    context = {'form': form,'posts':posts}
    return render(request, 'index/index.html', context)

def archive(request):
    
    posts = ArchivePost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index/archive.html', {'posts': posts})

def about(request):
    return render(request, 'index/about.html', {})