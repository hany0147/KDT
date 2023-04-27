
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from posts.models import Post

# 로그인
def login(request):
    if request.user.is_authenticated:
        # 인덱스로 나타내기
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()

    all_count = Post.objects.all().count()
    dev_count = Post.objects.filter(category='개발').count()
    cs_count = Post.objects.filter(category='CS').count()
    newT_count = Post.objects.filter(category='신기술').count()
    context = {
        'form': form,
        'all_count': all_count,
        'dev_count': dev_count,
        'cs_count': cs_count,
        'newT_count': newT_count,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
            
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserCreationForm()
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
    return render(request, 'accounts/signup.html', context)


@login_required
def mypage(request):
    all_count = Post.objects.all().count()
    dev_count = Post.objects.filter(category='개발').count()
    cs_count = Post.objects.filter(category='CS').count()
    newT_count = Post.objects.filter(category='신기술').count()
    context = {
        'all_count': all_count,
        'dev_count': dev_count,
        'cs_count': cs_count,
        'newT_count': newT_count,
    }    
    return render(request, 'accounts/mypage.html', context)


@login_required
def delete(request):
    # print(dir(request.user))
    request.user.delete()
    return redirect('index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserChangeForm(instance=request.user)
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
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 변경시 세션 무효화 방지
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
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
    return render(request, 'accounts/change_password.html', context)