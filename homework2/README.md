# AI Acknowledgement
Ai assistance (Claude) was used to help template the HTML structure of the website alongside Bootstrap styling.
Revisions and further research of these topics was conducted to learn logic and real life application.

# -------------------- Running App Locally --------------------

### 1. Clone repo
git clone https://github.com/Marwinu/cs4300
cd cs4300/homework2

### 2. Run virtual environment
python3 -m venv myenv --system-site-packages
source myenv/bin/activate

### 3. Install dependencies and migrate
pip install -r requirements.txt
python panage.py migrate

## 4. Create a superuser
python manage.py createsuperuser
(follow the prompt)

## 5. Start application
python manage.py runserver 0.0.0.0:3000

Open browser and enter:
Locally: http://localhost:3000/api/pages/movies/
Devdu: https://app-<container-name>.devedu.io/api/pages/movies/ 

## 6. Browse and book movies
To book seats and view booking history a user must be logged in.
Use the superuser login created in step 4.

If a server error or redirection occurs, login first at 
http://localhost:3000/admin/

Then go back to the movies page to continue

# -------------------- Render Deployment --------------------

Live app available at:
https://marwin-movie-app.onrender.com/api/pages/movies/

(App may take several minutes to load) 

## 1. Admin Login
To book seats and view booking history on the live site, login first at:
https://marwin-movie-app.onrender.com/admin/

Username: admin
Password: admin123!

## 2. Browse and book movies
After logging in, go to the movies page:
https://marwin-movie-app.onrender.com/api/pages/movies/

Click Book Now on any movie, enter a seat number, and submit.
Booking history can be viewed by clicking My Bookings at the top right bar. 

## 3. API Endpoints
https://marwin-movie-app.onrender.com/api/movies/
https://marwin-movie-app.onrender.com/api/seats/
https://marwin-movie-app.onrender.com/api/bookings/

# -------------------- Testing --------------------

## Unit and Integration Tests
cd cs4300/homework2
source myenv/bin/activate
python manage.py test bookings

## Coverage Report
coverage run manage.py test bookings
coverage report

## BDD Tests
python manage.py behave