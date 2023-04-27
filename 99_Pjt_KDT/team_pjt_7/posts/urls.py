from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'), # 전체 글 띄우기
    path('create/', views.create, name='create'), # 글 작성(전체 글로 리다이렉트)
    path('<int:pk>/', views.detail, name='detail'), # 상세 조회(삭제, 수정 버튼)
    path('<int:pk>/delete/', views.delete, name='delete'), # 게시글 삭제
    path('<int:pk>/update/', views.update, name='update'), # 게시글 수정
    path('category/<str:subject>/', views.category, name='category'), # 게시글 분류
]