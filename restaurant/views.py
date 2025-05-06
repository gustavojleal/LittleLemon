from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from datetime import datetime
from rest_framework import permissions, generics, response
from rest_framework import viewsets as viewssets
from .models import Booking, Menu
from .serialazers import BookingSerializer, MenuSerializer, UserSerializer


class UserViewSet(viewssets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):  # Corrigido: 'self' como primeiro argumento
        context = super().get_context_data(**kwargs)
        context['current_year'] = datetime.now().year
        return context
      

class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Welcome to the Home Page</h1>")
      
class AboutView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Welcome to the About Page</h1>")

     
class BookingViewSet(viewssets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

      
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def get(self, request, *args, **kwargs):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return response.Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        return response.Response(serializer.errors, status=400)
        
class SingleMenuItemView(generics.DestroyAPIView):
      serializer_class = MenuSerializer
      def get(self, request, *args, **kwargs):
          pk = kwargs['pk']
          menu_item = get_object_or_404(Menu, pk=pk)
          serializer = MenuSerializer(menu_item)
          return response.Response(serializer.data)