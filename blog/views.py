from django.shortcuts import render
from .models import Post, ArchivePost
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

def index(request):
    posts = ArchivePost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    context = {'posts':posts}
    return render(request, 'blog/index.html', context)

def archive(request):
    
    posts = ArchivePost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/archive.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form })


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})