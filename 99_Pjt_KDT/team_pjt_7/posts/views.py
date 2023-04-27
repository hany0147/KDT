from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    posts = Post.objects.all()
    all_count = Post.objects.all().count()
    dev_count = Post.objects.filter(category='개발').count()
    cs_count = Post.objects.filter(category='CS').count()
    newT_count = Post.objects.filter(category='신기술').count()
    context = {
        'all_count': all_count,
        'dev_count': dev_count,
        'cs_count': cs_count,
        'newT_count': newT_count,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    all_count = Post.objects.all().count()
    dev_count = Post.objects.filter(category='개발').count()
    cs_count = Post.objects.filter(category='CS').count()
    newT_count = Post.objects.filter(category='신기술').count()
    context = {
        'all_count': all_count,
        'dev_count': dev_count,
        'cs_count': cs_count,
        'newT_count': newT_count,
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    all_count = Post.objects.all().count()
    dev_count = Post.objects.filter(category='개발').count()
    cs_count = Post.objects.filter(category='CS').count()
    newT_count = Post.objects.filter(category='신기술').count()
    context = {
        'all_count': all_count,
        'dev_count': dev_count,
        'cs_count': cs_count,
        'newT_count': newT_count,
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    all_count = Post.objects.all().count()
    dev_count = Post.objects.filter(category='개발').count()
    cs_count = Post.objects.filter(category='CS').count()
    newT_count = Post.objects.filter(category='신기술').count()
    context = {
        'all_count': all_count,
        'dev_count': dev_count,
        'cs_count': cs_count,
        'newT_count': newT_count,
        'form': form,
        'post': post,
    }
    return render(request, 'posts/update.html', context)    


@login_required
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')


def category(request, subject):
    posts = Post.objects.filter(category=subject)
    all_count = Post.objects.all().count()
    dev_count = Post.objects.filter(category='개발').count()
    cs_count = Post.objects.filter(category='CS').count()
    newT_count = Post.objects.filter(category='신기술').count()
    context = {
        'all_count': all_count,
        'dev_count': dev_count,
        'cs_count': cs_count,
        'newT_count': newT_count,
        'posts': posts,
    }
    return render(request, 'posts/category.html', context)


# def category_list(request):
#     # if문을 넣어서 현재 어떤 카테고리냐에 따라 구분하고
#     # 변수명은 일치시키고, 그 변수를 컨텍스트에 넣는다.
#     all_count = Post.objects.all().count()
#     dev_count = Post.objects.filter(category='개발').count()
#     cs_count = Post.objects.filter(category='CS').count()
#     newT_count = Post.objects.filter(category='신기술').count()
#     context = {
#         'all_count': all_count,
#         'dev_count': dev_count,
#         'cs_count': cs_count,
#         'newT_count': newT_count,
#     }
#     print(type(all_count))
#     return render(request, 'index.html', context)