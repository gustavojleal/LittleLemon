
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from rest_framework import permissions, generics, response
from rest_framework import viewsets as viewssets
from .models import Booking, Menu
from .serialazers import BookingSerializer, MenuSerializer, UserSerializer
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
        return render(request, 'index.html', {
            'form': form,
            'show_signup_modal': True  
        })
    return redirect('home')

              
class UserViewSet(viewssets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AboutView(TemplateView):

    template_name = 'about.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')

     
class BookingViewSet(viewssets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

      
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
      permission_classes = [permissions.IsAuthenticatedOrReadOnly]
      serializer_class = MenuSerializer
      def get(self, request, *args, **kwargs):
          pk = kwargs['pk']
          menu_item = get_object_or_404(Menu, pk=pk)
          serializer = MenuSerializer(menu_item)
          return response.Response(serializer.data)
      def delete(self, request, *args, **kwargs):
          menu_item = get_object_or_404(Menu, pk=kwargs['pk'])
          menu_item.delete()
          return response.Response(status=204)