class State(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='states/')
    description = models.TextField()

    def __str__(self):
        return self.name
class Place(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='places/')
    description = models.TextField()
    famous_for = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Hotel(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=100)
    address = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    available_rooms = models.IntegerField()
    image = models.ImageField(upload_to='hotels/')

    def __str__(self):
        return self.name
class CarRental(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='rentals')
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)  # Car, Bike
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rentals/')

    def __str__(self):
        return f"{self.vehicle_type} at {self.place.name}"


SERIALIZERS

from rest_framework import serializers
from .models import State, Place, Hotel, CarRental

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
class CarRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRental
        fields = '__all__'

views.py


class StateListView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class PlaceByStateView(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        state_id = self.kwargs['state_id']
        return Place.objects.filter(state_id=state_id)

class HotelByPlaceView(generics.ListAPIView):
    serializer_class = HotelSerializer

    def get_queryset(self):
        place_id = self.kwargs['place_id']
        return Hotel.objects.filter(place_id=place_id)

class CarByPlaceView(generics.ListAPIView):
    serializer_class = CarRentalSerializer

    def get_queryset(self):
        place_id = self.kwargs['place_id']
        return CarRental.objects.filter(place_id=place_id)

urls.py

from django.urls import path
from .views import StateListView, PlaceByStateView, HotelByPlaceView, CarByPlaceView

urlpatterns = [
    path('states/', StateListView.as_view(), name='state-list'),
    path('states/<int:state_id>/places/', PlaceByStateView.as_view(), name='place-by-state'),
    path('places/<int:place_id>/hotels/', HotelByPlaceView.as_view(), name='hotel-by-place'),
    path('places/<int:place_id>/cars/', CarByPlaceView.as_view(), name='car-by-place'),
]

