from django.contrib import admin
from .models import Hotel
from .models import TouristPlaces
from .models import Transportation
from .models import Guide
from .models import Destination
from .models import Event
from .models import Crime
from .models import Restaurants
from .models import District
from .models import Division
from .models import Room
from .models import Booking
#Register your models here.

admin.site.register(Transportation)
admin.site.register(TouristPlaces)
admin.site.register(Hotel)
admin.site.register(Guide)
admin.site.register(Crime)
admin.site.register(Restaurants)
admin.site.register(Event)
admin.site.register(District)
admin.site.register(Division)
admin.site.register(Destination)
admin.site.register(Room)
admin.site.register(Booking)

