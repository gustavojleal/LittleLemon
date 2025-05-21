
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from djoser.serializers import UserSerializer

from rest_framework import viewsets as viewssets, permissions, generics, response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from datetime import datetime

from .serializers import MenuSerializer, BookingSerializer
from .models import Booking, Menu
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm



def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@api_view(['POST'])
def custom_logout(request, *args, **kwargs):
    token = request.headers.get('Authorization', '').replace('Token ', '')
    try:
        token_obj = Token.objects.get(key=token)
        token_obj.delete()
        return Response({"response": "Successfully logged out."}, status=204)
    except Token.DoesNotExist:
        print("Token não encontrado")
        return Response({"data": "Invalid token."}, status=400)

@api_view(['POST'])
def login(request, *args, **kwargs):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(data=request.data)
        if form.is_valid():
            try:
                user = form.get_user()
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "token": token.key,
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    }
                }, status=200)
            except Exception as e:
                print(e)
                return Response({"detail": str(e)}, status=400)
        return Response(form.errors, status=400)


@api_view(['POST'])
def signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = CustomUserCreationForm(data = request.data)
        if form.is_valid():
            try:
              form.save()
              return JsonResponse({"detail": "User created successfully."}, status=201)
            except Exception as e:
              print(e)
              return Response({"detail": "e"}, status=400)
        return JsonResponse(form.errors, status=400)

          
@api_view(['POST', 'GET'])
def debug_request(request):
    # Imprime os cabeçalhos
    print("Headers:")
    for key, value in request.headers.items():
        print(f"{key}: {value}")

    # Imprime os parâmetros da URL (GET)
    print("\nGET Parameters:")
    for key, value in request.GET.items():
        print(f"{key}: {value}")

    # Imprime os dados do corpo da requisição (POST, PUT, etc.)
    # print("\nPOST Data:")
    # for key, value in request.POST.items():
    #     print(f"{key}: {value}")

    # Imprime os cookies
    # print("\nCookies:")
    # for key, value in request.COOKIES.items():
    #     print(f"{key}: {value}")

    # # Imprime o corpo bruto da requisição
    # print("\nRaw Body:")
    # print(request.body.decode('utf-8'))

    # Retorna uma resposta JSON com os dados do request para depuração
    return JsonResponse({
        "headers": dict(request.headers),
        "get_params": dict(request.GET),
        # "post_data": dict(request.POST),
        # "cookies": dict(request.COOKIES),
        "raw_body": request.body.decode('utf-8'),
    })
        
class UserViewSet(viewssets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    return render(request, 'base.html')


class AboutView(TemplateView):
    template_name = 'about.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')

    # permission_classes = [permissions.IsAuthenticated] 
class BookingViewSet(APIView):
    def get(self, request, *args, **kwargs):
        try:
            date = request.GET.get('date', None)
            booking_date = datetime.strptime(date, "%Y-%m-%d").date()
            queryset = Booking.objects.filter(Booking_Date=booking_date)
            # queryset = Booking.objects.all()
            serializer = BookingSerializer(queryset, many=True)
            return JsonResponse({"data": serializer.data})
        except ValueError:
            print("deu pau")
            return JsonResponse({"error": "Formato de data inválido"})
      
class MenuItemsView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAuthenticated]
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        return response.Response(serializer.errors, status=400)
        
