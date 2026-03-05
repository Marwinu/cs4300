from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from . import views

router = DefaultRouter()
router.register(r'movies', MovieViewSet)    # /api/movies/
router.register(r'seats', SeatViewSet)      # /api/seats/
router.register(r'bookings', BookingViewSet)    # /api/bookings/

urlpatterns = [
    # HTML template pages
    path('', include(router.urls)),
    path('pages/movies/', views.movie_list_view, name='movie_list'),
    path('pages/movies/<int:movie_id>/book/', views.seat_booking_view, name='book_seat'),
    path('pages/bookings/history/', views.booking_history_view, name='booking_history'),
]