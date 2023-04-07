from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    data = request.GET.get('q')
    context = {
        'data': data,
    }
    return render(request, 'articles/catch.html', context)