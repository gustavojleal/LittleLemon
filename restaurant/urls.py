from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views



urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('', views.IndexView.as_view(), name = 'index'),
  path('home/', views.IndexView.as_view(), name = 'home'),
  path('about/', views.AboutView.as_view(), name = 'about'),
  path('menu/', views.MenuItemsView.as_view(), name = 'menu'),
  path('booking/', views.BookingViewSet.as_view(({'get': 'list', 'post': 'create'})), name = 'booking-list'),
  path('booking/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
  
]

