from django.urls import path
from . import views

app_name = 'nums'
urlpatterns = [
    path('nums/', views.index, name='nums_index'),
    path('number-print/<int:number>/', views.number_print, name='number-print'),
    path('calculate/<int:number1>/<int:number2>/', views.calculate, name='calculate'),
]
