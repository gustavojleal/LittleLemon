from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views



urlpatterns = [
  path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
  path('', views.IndexView.as_view(), name = 'index'),
  path('home/', views.HomeView.as_view(), name = 'home'),
  path('about/', views.AboutView.as_view(), name = 'about'),
  path('menu', views.MenuItemsView.as_view(), name = 'menu'),
  path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name = 'menu-detail'),
]

