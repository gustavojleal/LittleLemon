from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu

class MenuTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
       
        self.menu_item_1 = Menu.objects.create(title="Pizza", price=12.99, inventory=10)
        self.menu_item_2 = Menu.objects.create(title="Burger", price=8.99, inventory=5)

    def test_get_menu_items(self):
        url = reverse('menu')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
        self.assertEqual(response.data[0]['title'], "Pizza")
        self.assertEqual(response.data[1]['title'], "Burger")

    def test_create_menu_item(self):
        url = reverse('menu')
        data = {
            "title": "Pasta",
            "price": 10.99,
            "inventory": 15
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)
        self.assertEqual(Menu.objects.last().title, "Pasta")