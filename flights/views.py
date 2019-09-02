from .models import Flight, Booking
from .serializers import FlightSerializer,BookingSerializer
from rest_framework.generics import ListAPIView
from django.utils import timezone



class Flights(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class Bookings(ListAPIView):
	queryset = Booking.objects.filter(date__gte = timezone.now())
	serializer_class = BookingSerializer