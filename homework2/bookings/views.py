from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, get_object_or_404, redirect

# Viewsets, handles CRUD
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()       # gets movies from the database
    serializer_class = MovieSerializer   # converts to JSON

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()       # gets movies from the database
    serializer_class = SeatSerializer   # converts to JSON

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()       # gets movies from the database
    serializer_class = BookingSerializer   # converts to JSON

# HTML Template Views

def movie_list_view(request):
    movies = Movie.objects.all()   # gets all the movies
    return render(request, 'bookings/movie_list.html', {'movies': movies})   # pass to template


def seat_booking_view(request, movie_id):
    # if a user is not logged in then redirect
    if not request.user.is_authenticated:
        return redirect(f'/admin/login/?next=/api/pages/movies/{movie_id}/book/')

    movie = get_object_or_404(Movie, id=movie_id)   # gets the movie or returns a 404

    if request.method == 'POST':
        seat_number = request.POST.get('seat_number')

        # gets the a existing seat or creates one 
        seat, created = Seat.objects.get_or_create(
            seat_number=seat_number,
            booking_status=False
        )

        # creates booking linking movie, seat, user
        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user
        )

        return redirect('booking_history')   # goes to booking history (adter booking)

    return render(request, 'bookings/seat_booking.html', {'movie': movie})


def booking_history_view(request):
     # if a user is not logged in then redirect
    if not request.user.is_authenticated:
        return redirect('/admin/login/?next=/api/pages/bookings/history/')
    bookings = Booking.objects.filter(user=request.user)   # gets all bookings for the user
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})   # pass to template