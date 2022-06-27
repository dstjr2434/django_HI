from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.hello, name='index'),
    path('<int:page_number>/', views.page),
    path('helloname/',views.html),
    path('welcome/',views.welcome),
]