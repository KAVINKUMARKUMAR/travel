from .views import RegisterView,LoginView,LogoutView,DestinationList
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),  # 👈 new
    path('api/destinations/', DestinationList.as_view(), name='destination'),
]
