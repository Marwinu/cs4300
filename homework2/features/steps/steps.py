from behave import given, when, then
from django.contrib.auth.models import User
from bookings.models import Movie, Seat

@given('the application is running')
def step_app_running(context):
    """Just shows the app is running"""
    pass

@when('a user checks the movie page')
def step_check_movie_page(context):
    """Send GET request to movies endpoint"""
    context.response = context.test.client.get('/api/movies/')

@then('the page should successfully load')
def step_page_loads(context):
    """200 meaning it loaded"""
    assert context.response.status_code == 200

@when('a user submits a movie')
def step_submit_movie(context):
    """Send POST request with movie data"""
    data = {
        "title": "BDD Movie",
        "description": "BDD Test Description",
        "release_date": "2026-03-03",
        "duration": 120
    }
    context.response = context.test.client.post('/api/movies/', data)

@then('a movie should be created')
def step_movie_created(context):
    """Check movie was created, returned 201"""
    assert context.response.status_code == 201

@when('a user checks the seats page')
def step_check_seats_page(context):
    """Send GET request to seats endpoint"""
    context.response = context.test.client.get('/api/seats/')

@when('a user submits a booking')
def step_submit_booking(context):
    """Create user, movie and seat then POST a new booking"""
    user = User.objects.create_user(
        username="testbehaveuser", password="passwordbehave"
    )
    movie = Movie.objects.create(
        title="BDD Movie",
        description="BDD Test",
        release_date="2026-03-03",
        duration=90
    )
    seat = Seat.objects.create(
        seat_number=1,
        booking_status=False
    )
    data = {
        "movie": movie.id,
        "seat": seat.id,
        "user": user.id
    }
    context.response = context.test.client.post('/api/bookings/', data)

@then('a booking should be created')
def step_booking_created(context):
    """Check booking was created, returned 201"""
    assert context.response.status_code == 201