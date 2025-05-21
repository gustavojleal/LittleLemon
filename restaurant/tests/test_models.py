# restaurant/tests/test_models.py
import pytest
from restaurant.models import Booking, Menu
from django.utils import timezone

@pytest.mark.django_db
def test_booking_model():
    # Tests Booking model creation and string representation
    booking = Booking.objects.create(
        name="John Doe",
        No_of_guests=4,
        Booking_Date=timezone.now().date()
    )
    assert str(booking) == "John Doe"  # Validate __str__ method
    assert booking.No_of_guests == 4   # Validate guest count

@pytest.mark.django_db
def test_menu_model():
    # Tests Menu model creation and string representation
    menu = Menu.objects.create(
        title="Pizza",
        price=9.99,
        inventory=10
    )
    assert str(menu) == "Pizza : 9.99"  # Validate __str__ method
    assert menu.inventory == 10         # Validate inventory value