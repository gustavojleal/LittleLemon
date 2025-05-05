from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):  # Corrigido: 'self' como primeiro argumento
        context = super().get_context_data(**kwargs)
        context['current_year'] = datetime.now().year
        return context
      

class homeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Welcome to the Home Page</h1>")