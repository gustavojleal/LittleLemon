from django.urls import path, re_path
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),  # Rota principal
    re_path(r'^.*$', views.index, name='react_routes'),  # Redireciona todas as rotas para o React
]




