from django.urls import path
from . import views


urlpatterns = [
  path('', views.IndexView.as_view(), name = 'index'),
  path('home/', views.HomeView.as_view(), name = 'home'),
  path('about/', views.AboutView.as_view(), name = 'about'),
  path('menu', views.MenuItemsView.as_view(), name = 'menu'),
  path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name = 'menu-detail'),
  path('tables/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='table-detail'),
]

