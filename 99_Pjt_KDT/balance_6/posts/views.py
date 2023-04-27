from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    per_page = 5
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page)
    last = paginator.num_pages
    context = {
        'posts': page_obj,
        'last' : last,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)

    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)



def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    last = Post.objects.last()
    comment_form = CommentForm()
    comments = post.comment_set.all()
    context = {
        'post': post,
        'last': last,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('posts:index')

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:detail', post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('posts:index')
    context = {
        'post' : post,
        'form' : form,
    }
    return render(request, 'posts/update.html', context)




@login_required
def answer(request, post_pk, answer):
    # POST posts/<int:post_pk>/answer/<str:answer>/
    post = Post.objects.get(pk=post_pk)
    user = request.user
    if request.method == "POST":
        if user in post.select1_users.all() or user in post.select2_users.all():
            pass
        else:
            if answer == post.select1_content:
                post.select1_users.add(user)
                is_select = True
                context = {
                    'is_select' : is_select,
                    'select1_count': post.select1_users.count()
                }
                
            elif answer == post.select2_content:
                post.select2_users.add(user)
                is_select = True
                context = {
                    'is_select' : is_select,
                    'select2_count': post.select2_users.count()
                }
            return JsonResponse(context)
    return redirect('posts:detail', post_pk, context)


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()

        return redirect('posts:detail', post.pk)

    context = {
        'post': post,
        'comment_form' : comment_form,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if request.user == comment.user:
        # 댓글 삭제
        comment.delete()
    return redirect('posts:detail', post_pk)


def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'likes_count': post.like_users.count()
    }
    return JsonResponse(context)
    