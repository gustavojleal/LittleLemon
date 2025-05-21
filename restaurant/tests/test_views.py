# restaurant/tests/test_views.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from restaurant.models import Booking, Menu

@pytest.mark.django_db
def test_menu_items_view_authentication():
    # Tests authentication requirements for MenuItemsView
    client = APIClient()
    
    # Unauthenticated request should return 401 (Unauthorized)
    # because authentication credentials are missing
    response = client.get(reverse('menu'))
    assert response.status_code == 401  # Updated from 403 to 401
    
    # Authenticate user and retry
    user = User.objects.create_user(username='testuser', password='testpass')
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = client.get(reverse('menu'))
    assert response.status_code == 200  # OK for authenticated users

@pytest.mark.django_db
def test_booking_viewset():
    # Tests CRUD operations for BookingViewSet
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpass')
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    # Test POST (create booking)
    data = {
        "name": "Test Booking",
        "No_of_guests": 3,
        "Booking_Date": "2024-01-01"
    }
    response = client.post(reverse('booking-list'), data)
    assert response.status_code == 201  # Created
    assert Booking.objects.count() == 1

    # Test GET (list bookings)
    response = client.get(reverse('booking-list'))
    assert len(response.data) == 1  # Verify one booking exists

@pytest.mark.django_db
def test_signup_view(client):
    # Tests user signup functionality
    data = {
        "username": "newuser",
        "password1": "complexpass123",
        "password2": "complexpass123"
    }
    response = client.post(reverse('signup'), data)
    assert response.status_code == 302  # Redirect after successful signup
    assert User.objects.filter(username="newuser").exists()  # Verify user creation