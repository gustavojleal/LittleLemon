from django.urls import path
from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name = 'index'),
  path('home/', views.homeView.as_view(), name = 'home'),
]
