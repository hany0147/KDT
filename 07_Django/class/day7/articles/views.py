from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    from .models import Article
    
    #1
    # 이 친구는 너무 기니까 ^^
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2(권장)
    article = Article(title = title, content = content)
    # 저장 전 유효성 검사해야 함 / 즉, 추가 작업을 위해 2번 방법 채택
    article.save()

    #3
    # 검사할 타이밍이 안나옴
    # Article.objects.create(title = title, content = content)

    return render(request, 'articles/create.html') 