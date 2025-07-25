from django.db import models
from django.contrib.auth.models import User

################################################################################
# 1. State
################################################################################
class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


################################################################################
# 2. Place (City or Area)
################################################################################
class Place(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return f"{self.name}, {self.state.name}"


################################################################################
# 3. Amenity (used for Hotels and Rooms)
################################################################################
class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='amenity_icons/', blank=True, null=True)  # optional icon/image

    def __str__(self):
        return self.name


################################################################################
# 4. Hotel
################################################################################
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='hotels')
    main_image = models.ImageField(upload_to='hotels/', null=True, blank=True)
    star_rating = models.PositiveSmallIntegerField(default=1)  # 1 to 5 stars
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='hotels')
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    map_url = models.URLField(blank=True)  # Google Maps or similar location link

    def __str__(self):
        return self.name


################################################################################
# 5. HotelImage (multiple images per hotel)
################################################################################
class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotels/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.hotel.name}"


################################################################################
# 6. RoomType or Category (optional abstraction for room categories)
################################################################################
class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


################################################################################
# 7. Room
################################################################################
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    category = models.ForeignKey(RoomCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='rooms')
    name = models.CharField(max_length=100, blank=True)  # e.g., Deluxe Room, King Suite
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()  # Number of guests the room accommodates
    is_available = models.BooleanField(default=True)
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='rooms')
    main_image = models.ImageField(upload_to='rooms/', blank=True, null=True)

    def __str__(self):
        return f"{self.name or self.category} at {self.hotel.name}"


################################################################################
# 8. RoomImage (for multiple images of rooms)
################################################################################
class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='rooms/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.room}"


################################################################################
# 9. Booking
################################################################################
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    guests_adults = models.PositiveIntegerField(default=1)
    guests_children = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.user.username} ({self.status}) at {self.hotel.name}"


################################################################################
# 10. Review (Hotel Reviews)
################################################################################
class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=5)  # 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.hotel.name} by {self.user}"


################################################################################
# 11. Policy (Hotel policies, optional)
################################################################################
class Policy(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='policies')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} for {self.hotel.name}"













Overall Style & Layout
Use a clean white/light background with blue accent colors for clickable elements (buttons, links).

Maintain ample whitespace and padding around sections for neat separation.

The page should be responsive, with a sticky booking widget on desktop, and a simple floating book button on mobile.

Use modern sans-serif fonts with clear hierarchy: large titles, smaller subtitles, readable body text.

Add subtle shadows and rounded corners to cards, buttons, and widgets for visual depth.

Use consistent icons for amenities and interactive elements (favorite, rating stars).

1. Header (Sticky)
Place a full-width header at the top with:

Logo/Brand name at the left.

Main navigation links (Home, Hotel List, Bookings, Support).

User profile or login/register on the right.

Use a white background with dark text; highlight current page with blue accent.

2. Main Content (Vertically Stacked)
A. Hotel Gallery / Image Carousel (Top Banner)
Large carousel showing high-quality images: hotel exterior, rooms, lobby, amenities.

Include navigation arrows and image indicators (dots).

Optional virtual tour or video icon overlay on images.

On mobile, enable swipe gestures and responsive resizing.

B. Hotel Info Header (Below Gallery)
Hotel name prominently displayed in large font.

Star rating with visible star icons (1 to 5).

Location details: place and state with clickable map link or button.

Save/favorite icon (heart/bookmark) placed top-right of this section.

A thin divider line underneath for separation.

C. Booking Widget (Right Sidebar - Desktop Sticky)
Box with light background and subtle shadow, fixed on the right side desktop view.

Include:

Date selectors for check-in and check-out.

Guest selectors for adults and children.

Real-time price calculation (price/night and total).

Prominent "Book Now" button in blue with white text.

Cancellation policy brief note or icon (e.g., "Free Cancellation").

On mobile, relocate widget to top or bottom with a floating booking button.

D. Quick Description & Highlights
Short description paragraph (2-3 sentences) about the hotel.

Highlighted badges or key selling points (e.g., “Great Location”, “Breakfast Included”, “Eco-Friendly”).

Optional badges for awards or certifications with small icons.

E. Amenities At a Glance
A horizontal grid or row of amenity icons with labels: Wi-Fi, Pool, Parking, Restaurant, Gym, etc.

"See all amenities" link or button to expand the full list in a modal or below.

F. Room Types and Availability
List or grid of rooms available for the selected dates.

Each room card includes:

Room main image thumbnail.

Room name/type, short description.

Capacity and amenities icons.

Price per night and any discount badge.

“Select Room” or “Book” button.

Clicking/selecting opens a booking form/modal or expands to show detailed info.

G. Additional Tabbed Sections (Below Rooms)
Use tabs or accordion style for the following:

Description: Full hotel and service details.

Amenities: Expanded amenity list, possibly categorized.

Reviews: Guest reviews with rating summary and filtering.

Location: Embedded interactive map with hotel location and key attractions.

Policies: Check-in/out times, cancellation terms, payment methods, house rules.

FAQs: Common guest questions and answers.

3. Footer (Bottom of Page)
Contains:

Contact info (phone, email).

Social media icons and links.

Secondary navigation links: Terms of Service, Privacy Policy, Support.

Styled with a light background and smaller font size.

Additional Guidance
Sticky elements (header and booking widget) ensure accessibility during scroll.

Buttons and icons should have hover/focus states for interactivity.

Use meaningful alt-text for images and accessible labels for interactive controls.

Manage loading states gracefully with placeholders or skeletons.

Include subtle microinteractions for better user engagement (e.g., button clicks, tab changes, favorite toggles). create a react frontend based on this prompt give the code
