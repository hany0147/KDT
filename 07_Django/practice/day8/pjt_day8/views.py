from django.shortcuts import render

def base_index(request):
    return render(request, 'index.html')