Super Kavin! 🔥
Here’s your detailed and powerful prompt to create a fully functional and responsive Flight Booking Homepage using ReactJS (single component) with separate CSS file. I’ve included everything a frontend developer or AI code generator will need to create a professional UI. 🙌


---

🧾 Detailed Prompt to Create Flight Booking Homepage

> 💬 Prompt:
Create a responsive flight booking homepage using ReactJS. All layout and structure should be in a single React component (e.g. HomePage.jsx), and all styles should be written in a separate CSS file (e.g. HomePage.css) and imported into the component.



The homepage must include the following sections in order:


---

🔷 1. Header / Navigation Bar

Fixed/sticky at the top.

Logo on the left with icon and text (e.g., ✈️ SkyFly).

Navigation links on the right:

Home, Flights, Offers, Contact, Login / Signup.


Responsive hamburger menu for smaller screens.



---

🔷 2. Hero Section (Banner)

Fullscreen background image (air travel related).

Overlay with:

Big Title: “Find & Book Your Flight Easily”

Subtitle: “Search from 100+ airlines for the best deals”

Button: “Search Flights”


Button scrolls to search section (onClick scroll effect).



---

🔷 3. Flight Search Section (Main Form)

Card-style form layout with white background and shadow.

Fields to include:

From (input with airport city)

To (input with airport city)

Departure Date (input type="date")

Return Date (optional)

Passengers (number input or dropdown)

Search Flights (primary button)


Make the form responsive and aligned in one row (on desktop) or column (on mobile).



---

🔷 4. Popular Routes Section

Title: "Popular Routes"

Grid of cards (3 or 4 per row)

Each card includes:

Image of destination

Route name (e.g., Chennai → Delhi)

Price tag (e.g., “From ₹2,499”)


Use hover effect on cards (e.g., slight scale or shadow).



---

🔷 5. Why Choose Us Section

Title: “Why Choose Us?”

Display 3 or 4 feature blocks with icons:

✈️ 100+ Airlines

🔒 Secure Payment

💸 Best Price Guarantee

📞 24/7 Support


Use flexbox or grid and icons (can be emoji or font-awesome).



---

🔷 6. Testimonials Section

Title: "What Our Customers Say"

Display 2 or 3 cards with:

Customer image (placeholder or avatar)

Name

Short quote or review


Use clean, card-based layout with box-shadow.



---

🔷 7. Footer Section

Background in dark grey/navy blue.

Include:

Company info (e.g., © 2025 SkyFly. All Rights Reserved.)

Links: About Us, Terms, Privacy, Help Center

Social icons: Facebook, Twitter, Instagram (use emoji or placeholders)


Responsive and cleanly spaced.



---

🧑‍💻 Tech Details:

Use plain CSS in HomePage.css (no Tailwind or inline styles).

Import the CSS file into the component: import './HomePage.css';

Use semantic HTML5 tags (<section>, <header>, <footer>, etc.)

Ensure mobile-first responsiveness using media queries.

Use dummy content and placeholders where needed.



---

⚙️ Folder Structure:

src/
 └── components/
      ├── HomePage.jsx
      └── HomePage.css





 from django.db import models
from django.contrib.auth.models import AbstractUser

# Extend user model to support roles
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True)

class Airport(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Flight(models.Model):
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10, unique=True)
    departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    price_per_seat = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('on_time', 'On Time'), ('delayed', 'Delayed'), ('cancelled', 'Cancelled')
    ], default='on_time')

class Passenger(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    id_document = models.CharField(max_length=100)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passengers = models.ManyToManyField(Passenger)
    seats_booked = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')
    ], default='confirmed')
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')
    ], default='pending')


from rest_framework import serializers
from .models import Flight, Booking, Passenger, Airport

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    departure_airport = AirportSerializer()
    arrival_airport = AirportSerializer()

    class Meta:
        model = Flight
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True)

    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        passengers_data = validated_data.pop('passengers')
        booking = Booking.objects.create(**validated_data)
        for passenger_data in passengers_data:
            passenger = Passenger.objects.create(**passenger_data)
            booking.passengers.add(passenger)
        # update flight seat count
        flight = booking.flight
        flight.available_seats -= booking.seats_booked
        flight.save()
        return booking




from rest_framework import viewsets, permissions
from .models import Flight, Booking, Airport
from .serializers import FlightSerializer, BookingSerializer, AirportSerializer

class AirportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class FlightViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_queryset(self):
        from_city = self.request.query_params.get('from')
        to_city = self.request.query_params.get('to')
        date = self.request.query_params.get('date')
        qs = Flight.objects.all()
        if from_city and to_city and date:
            qs = qs.filter(
                departure_airport__city__icontains=from_city,
                arrival_airport__city__icontains=to_city,
                departure_time__date=date
            )
        return qs

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, BookingViewSet, AirportViewSet

router = DefaultRouter()
router.register('flights', FlightViewSet, basename='flights')
router.register('bookings', BookingViewSet, basename='bookings')
router.register('airports', AirportViewSet, basename='airports')

urlpatterns = [
    path('api/', include(router.urls)),
]