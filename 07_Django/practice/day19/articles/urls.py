from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_total),
    path('articles/<article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('comments/', views.comment_total),
    path('comments/<int:comment_pk>/', views.comment_detail),
]