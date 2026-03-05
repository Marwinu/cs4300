from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from rest_framework.test import APIClient

# Unit Testing ----

class MovieModelTest(TestCase):
    def setUp(self):
        """Before each test, create a test movie"""
        self.movie = Movie.objects.create(
            title="Generic Movie Title",
            description="Test Description",
            release_date="2026-03-03",
            duration=120
        )

    # Happy path - Movies

    def test_movie_title(self):
        """Check for matching titles"""
        self.assertEqual(self.movie.title, "Generic Movie Title")

    def test_movie_desc(self):
        """Check for matching description"""
        self.assertEqual(self.movie.description, "Test Description")

    def test_movie_duration(self):
        """Check for matching duration"""
        self.assertEqual(self.movie.duration, 120)

    def test_movie_duration_int(self):
        """Check duration is an integer"""
        self.assertIsInstance(self.movie.duration, int)

    # Edge cases - Movies

    def test_movie_zero_dur(self):
        """What if someone enters 0 for duration?"""
        movie = Movie.objects.create(
            title="Short Movie",
            description="No duration",
            release_date="2026-03-03",
            duration=0
        )
        self.assertEqual(movie.duration, 0)

    def test_movie_long_desc(self):
        """What if a long description is entered?"""
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
        """Create a test seat"""
        self.seat = Seat.objects.create(
            seat_number=1,
            booking_status=False  # means seat is available
        )

    # Happy path - seat

    def test_seat_num(self):
        """Checking seat number"""
        self.assertEqual(self.seat.seat_number, 1)

    def test_seat_available(self):
        """Checking booking status"""
        self.assertFalse(self.seat.booking_status)

    def test_seat_bool(self):
        """Checking booking status type"""
        self.assertIsInstance(self.seat.booking_status, bool)

    # Edge cases - seat

    def test_seat_booked(self):
        """Changing status of booking test"""
        self.seat.booking_status = True
        self.seat.save()  # saves data
        self.assertTrue(self.seat.booking_status)

    def test_seat_num_int(self):
        """Checking seat number is an integer"""
        self.assertIsInstance(self.seat.seat_number, int)


class BookingModelTest(TestCase):
    def setUp(self):
        """Bookings need a user, movie, and seat"""
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
        """Making sure the booking exists"""
        self.assertIsNotNone(self.booking)

    def test_booking_movie(self):
        """The booking should point to our test movie"""
        self.assertEqual(self.booking.movie.title, "Booking Test Movie")

    def test_booking_user(self):
        """The booking should belong to bookinguser"""
        self.assertEqual(self.booking.user.username, "bookinguser")

    # Edge cases - booking

    def test_booking_multi(self):
        """Tests creating another booking with the same user"""
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

# Integration Testing ----

class MovieAPITest(TestCase):
    def setUp(self):
        """Before each test, create an API client and test movie"""
        self.client = APIClient()  # simulates API requests
        self.movie = Movie.objects.create(
            title="API Movie",
            description="API Test",
            release_date="2026-03-03",
            duration=90
        )

    # Happy path - Movies API

    def test_get_movies(self):
        """Check GET /api/movies/ returns 200 OK"""
        response = self.client.get('/api/movies/')  # send GET request
        self.assertEqual(response.status_code, 200)  # 200 means success

    def test_post_movie(self):
        """Check POST /api/movies/ creates a new movie and returns 201"""
        data = {
            "title": "New Movie",
            "description": "New Description",
            "release_date": "2026-03-03",
            "duration": 100
        }
        response = self.client.post('/api/movies/', data)  # send POST request
        self.assertEqual(response.status_code, 201)  # 201 means created

    def test_movies_json(self):
        """Check the API returns JSON format not HTML"""
        response = self.client.get('/api/movies/')  # send GET request
        self.assertEqual(response['Content-Type'], 'application/json')  # check format is JSON


class SeatAPITest(TestCase):
    def setUp(self):
        """Before each test, create an API client"""
        self.client = APIClient()  # simulates API requests

    # Happy path - Seats API

    def test_get_seats(self):
        """Check GET /api/seats/ returns 200 OK"""
        response = self.client.get('/api/seats/')  # send GET request
        self.assertEqual(response.status_code, 200)  # 200 means success

    def test_post_seat(self):
        """Check POST /api/seats/ creates a new seat and returns 201"""
        data = {"seat_number": 5, "booking_status": False}
        response = self.client.post('/api/seats/', data)  # send POST request
        self.assertEqual(response.status_code, 201)  # 201 means created

    def test_seats_json(self):
        """Check the API returns JSON format not HTML"""
        response = self.client.get('/api/seats/')  # send GET request
        self.assertEqual(response['Content-Type'], 'application/json')  # check format is JSON


class BookingAPITest(TestCase):
    def setUp(self):
        """Before each test, create an API client, user, movie and seat"""
        self.client = APIClient()  # simulates API requests
        self.user = User.objects.create_user(
            username="testuser", password="pass123"
        )
        self.movie = Movie.objects.create(
            title="API Movie",
            description="API Test",
            release_date="2026-03-03",
            duration=90
        )
        self.seat = Seat.objects.create(
            seat_number=1,
            booking_status=False
        )

    # Happy path - Bookings API

    def test_get_bookings(self):
        """Check GET /api/bookings/ returns 200 OK"""
        response = self.client.get('/api/bookings/')   # send GET request
        self.assertEqual(response.status_code, 200)  # 200 means success

    def test_post_booking(self):
        """Check POST /api/bookings/ creates a new booking and returns 201"""
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }
        response = self.client.post('/api/bookings/', data)  # send POST request
        self.assertEqual(response.status_code, 201)  # 201 means created

    def test_bookings_json(self):
        """Check the API returns JSON format not HTML"""
        response = self.client.get('/api/bookings/')  # send GET request
        self.assertEqual(response['Content-Type'], 'application/json')  # check format is JSON


class HTMLViewTest(TestCase):
    def setUp(self):
        """Before each test, create a user and movie for HTML view tests"""
        self.client = APIClient()  # simulates requests
        self.user = User.objects.create_user(
            username="testuser", password="pass123"
        )
        self.movie = Movie.objects.create(
            title="HTML Movie",
            description="HTML Test",
            release_date="2026-03-03",
            duration=90
        )

    def test_movie_list_page(self):
        """Check the movie list page loads correctly"""
        response = self.client.get('/api/pages/movies/')  # send GET request
        self.assertEqual(response.status_code, 200)  # 200 means page loaded

    def test_seat_booking_page(self):
        """Check the seat booking page loads for a valid movie"""
        response = self.client.get(f'/api/pages/movies/{self.movie.id}/book/')  # send GET with movie id
        self.assertEqual(response.status_code, 200)  # 200 means page loaded

    def test_booking_history_page(self):
        """Check the booking history page loads correctly"""
        self.client.login(username="testuser", password="pass123")  # log in first
        response = self.client.get('/api/pages/bookings/history/')  # send GET request
        self.assertEqual(response.status_code, 200)  # 200 means page loaded