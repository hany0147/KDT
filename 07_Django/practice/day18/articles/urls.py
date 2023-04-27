from django.urls import path
from . import views
urlpatterns = [
    path('', views.article_home),
    path('<int:article_pk>/', views.article_detail),
]