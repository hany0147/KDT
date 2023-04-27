from django.shortcuts import render
from posts.models import Post

def index(request):
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
    return render(request, 'index.html', context)
    

