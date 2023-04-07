from django.urls import path
# 명시적 상대 경로(django 권장사항)를 위해 from .을 기입
from . import views # 같은 위치에 있으니까

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail, name='detail'),
    path('greeting/<name>/', views.greeting, name='greeting'),
]
