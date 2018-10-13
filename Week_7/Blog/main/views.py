from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html")

def show_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, "post/show.html", context)

def post_details(request, id):
    post = Post.objects.get(pk=id)
    comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, "post/details.html", context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('show_posts')
    form = PostForm
    context = {
        'form': form,
    }
    return render(request, "post/add.html", context)

def update_post(request, id):
    instance = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post_details', id)
        else:
            error = "someethin not validdate"
            context = {
            'form': form,
            'name': instance.title,
            'id': id,
            'error': error,
            }
            return render(request, 'post/update.html', context) 
    context = {
        'form': form,
        'name': instance.title,
        'id': id,
    }
    
    return render(request, 'post/update.html', context) 

def delete_post(request, id):
    Post.objects.get(pk=id).delete()
    return redirect('show_posts')


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            fk = form.cleaned_data['post'].id
            if request.user.is_authenticated:
                comment.user = request.user
            else:
                comment.user = User.objects.get(pk=3)
            comment.save()
            return redirect('post_details', fk)
    form = CommentForm()
    context = {
        'form': form,
    }
    return render(request, "comment/add.html", context)

def update_comment(request, id):
    instance = get_object_or_404(Post, pk=id)
    form = CommentForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            fk = form.cleaned_data['post'].id
            return redirect('post_details', fk)
        else:
            error = "someethin not validdate"
            context = {
            'form': form,
            'name': instance.title,
            'id': id,
            'error': error,
            }
            return render(request, 'comment/update.html', context) 
    context = {
        'form': form,
        'id': id,
    }
    
    return render(request, 'comment/update.html', context) 

def delete_comment(request, id):
    fk = Comment.objects.get(pk=id).post.id
    Comment.objects.get(pk=id).delete()
    return redirect('post_details', fk)

