from django.contrib.auth.models import User
from django.contrib import admin
from . import models

admin.site.register([models.Booking, models.Menu])
