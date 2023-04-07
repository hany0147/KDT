from django.shortcuts import render

# Create your views here.

def today_dinner(request):
    import random
    foods = ['치킨', '커리', '햄버거', '피자', '우동', '국밥', '김치찌개', '초밥', '제육덮밥']
    boojangnim = ['국밥', '김치찌개', '제육덮밥']
    context = {
        # 'foods': foods,
        'foods': random.choice(foods),
        'boojangnim': boojangnim
    }
    return render(request, 'articles/today_dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data
    }
    return render(request, 'articles/catch.html', context)

def lotto_create(request):
    return render(request, 'articles/lotto_create.html')

def lotto(request):
    import random
    
    data = int(request.GET.get('lotto_nums'))
    lotto_number = []

    for _ in range(data):
        lotto = random.sample(range(1, 46), k=6)
        lotto_number.append(lotto)
    context = {
        'data': range(int(data)),
        'lotto_number': lotto_number
    }
    return render(request, 'articles/lotto.html', context)