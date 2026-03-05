from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, get_object_or_404, redirect

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# HTML Template Views

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking_view(request, movie_id):
    if not request.user.is_authenticated:
        return redirect(f'/admin/login/?next=/api/pages/movies/{movie_id}/book/')

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        seat_number = request.POST.get('seat_number')

        seat, created = Seat.objects.get_or_create(
            seat_number=seat_number,
            booking_status=False
        )

        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user
        )

        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie})


def booking_history_view(request):
    if not request.user.is_authenticated:
        return redirect('/admin/login/?next=/api/pages/bookings/history/')
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})