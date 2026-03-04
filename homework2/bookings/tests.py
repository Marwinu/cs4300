from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    def setUp(self):
        # Before each test, create a test movie
        self.movie = Movie.objects.create(
            title="Generic Movie Title",
            description="Test Description",
            release_date="2026-03-03",
            duration=120
        )

    # Happy path - Movies
    # Check for matching titles, description, duration, duration type
    def test_movie_title(self):
        # Check matching titles
        self.assertEqual(self.movie.title, "Generic Movie Title")

    def test_movie_desc(self):
        self.assertEqual(self.movie.description, "Test Description")

    def test_movie_duration(self):
        self.assertEqual(self.movie.duration, 120)

    def test_movie_duration_int(self):
        self.assertIsInstance(self.movie.duration, int)

    # Edge cases - Movies
    # Check for odd inputs 
    def test_movie_zero_dur(self):
        # What if someone enters 0?
        movie = Movie.objects.create(
            title="Short Movie",
            description="No duration",
            release_date="2026-03-03",
            duration=0
        )
        self.assertEqual(movie.duration, 0)

    def test_movie_long_desc(self):
        # What if a long description is entered?
        long_desc = "LongMessage" * 200
        movie = Movie.objects.create(
            title="Long Desc Movie",
            description=long_desc,
            release_date="2026-03-03",
            duration=120
        )
        self.assertEqual(len(movie.description), 2200)


class SeatModelTest(TestCase):
    def setUp(self):
        # Create a test seat
        self.seat = Seat.objects.create(
            seat_number=1,
            booking_status=False  # means seat is available
        )

    # Happy path - seat
    # Checking seat number, booking status and booking status type
    def test_seat_num(self):
        self.assertEqual(self.seat.seat_number, 1)

    def test_seat_available(self):
        self.assertFalse(self.seat.booking_status)

    def test_seat_bool(self):
        self.assertIsInstance(self.seat.booking_status, bool)

    # Edge cases - seat
    def test_seat_booked(self):
        # Changing status of booking test
        self.seat.booking_status = True
        self.seat.save()  # saves data
        self.assertTrue(self.seat.booking_status)  

    def test_seat_num_int(self):
        self.assertIsInstance(self.seat.seat_number, int)


class BookingModelTest(TestCase):
    def setUp(self):
        # Bookings need a user, movie, and seat
        self.user = User.objects.create_user(
            username="bookinguser", password="pass123"
        )
        self.movie = Movie.objects.create(
            title="Booking Test Movie",
            description="Booking Test Description",
            release_date="2026-03-03",
            duration=120
        )
        self.seat = Seat.objects.create(
            seat_number=1,
            booking_status=False
        )
        # Link user, movie, and seat into booking and create
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

    # Happy path - booking 
    def test_booking_exists(self):
        # Making sure the booking exists
        self.assertIsNotNone(self.booking)

    def test_booking_movie(self):
        # The booking should point to our test movie
        self.assertEqual(self.booking.movie.title, "Booking Test Movie")

    def test_booking_user(self):
        # The booking should belong to bookinguser
        self.assertEqual(self.booking.user.username, "bookinguser")

    # Edge cases - booking

    # tests creating another booking, with the same user
    def test_booking_multi(self):
        movie2 = Movie.objects.create(
            title="Scary Movie 2",
            description="Scary Desc",
            release_date="2026-03-03",
            duration=90
        )
        seat2 = Seat.objects.create(
            seat_number=2,
            booking_status=False
        )
        booking2 = Booking.objects.create(
            movie=movie2,
            seat=seat2,
            user=self.user  # same user
        )
        # is there 2 bookings? 
        bookings = Booking.objects.filter(user=self.user)
        self.assertEqual(len(bookings), 2)

#TODO integration testing