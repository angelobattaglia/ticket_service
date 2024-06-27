# Note: it is important to add "render_template" to the imports
from flask import Flask, render_template
from flask import Flask, render_template, request
from flask import redirect, url_for, flash, abort

# Flask-Login is a Flask extension that provides a framework for handling user authentication
import flask_login
from flask_login import LoginManager
from flask_login import login_required
# Logs a user in. We should pass the actual user object to this method:
# returns True if the log in attempt succeeds, and False if it fails
from flask_login import login_user

# Security and Forms for the login
import werkzeug.security as ws
# from forms import LoginForm

# Import the Image module from the PIL (Python Imaging Library) package. 
# Used to preprocess the images uploaded by the users. 
# Ensure 'Pillow' is installed before running the application by using
# the command 'pip install Pillow'
# from PIL import Image
# PROFILE_IMG_HEIGHT = 130
# POST_IMG_WIDTH = 300

# Import the datetime library to handle the pubblication date of the raccolte
import datetime

## Import the dao modules and the models module
import models
import utenti_dao
import trains_dao
import bookings_dao

## Here I call these functions for the creation of the DB tables at startup time
from table_creation import create_table_users, create_table_trains, create_table_bookings
create_table_users()
create_table_trains()
create_table_bookings()

## Calling the method to populate the DB
from populate import populate, populate_solutions
populate()
# populate_solutions()

# create the application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'gematria'


# This is for login_manager 
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    
    return render_template('home.html', title='Home')

#########################################################
#########################################################
#########################################################
########## I make the booking and search system #########
#########################################################
#########################################################
#########################################################
#########################################################

@app.route('/search_trains', methods=['POST'])
def search_trains():
    departure_city = request.form['departure_city']
    arrival_city = request.form['arrival_city']
    departure_date = request.form['departure_date']

    # Validate the form inputs
    if departure_city == arrival_city:
        flash('Departure city and arrival city cannot be the same.', 'danger')
        return redirect(url_for('home'))
    if datetime.datetime.strptime(departure_date, '%Y-%m-%d') < datetime.datetime.now():
        flash('Departure date cannot be in the past.', 'danger')
        return redirect(url_for('home'))

    # Search for trains
    results = trains_dao.search_trains(departure_city, arrival_city, departure_date)

    if not results:
        flash('No trains available for the selected route and date.', 'info')
    
    min_date = datetime.datetime.now().strftime('%Y-%m-%d')
    return render_template('home.html', title='Search Results', departure_city=departure_city, arrival_city=arrival_city, departure_date=departure_date ,min_date=min_date, trains=results)

# Booking form with dynamic routing
@app.route('/booking_form/<int:train_id>', methods=['GET'])
@flask_login.login_required
def booking_form(train_id):
    # Find the train by its ID
    train = None
    for t in trains_dao.get_trains():
        if t[0] == train_id:
            train = t
            break

    # Controllo che il treno sia stato trovato, in caso negativo faccio un redirect alla home
    if not train:
        flash('Train not found', 'danger')
        return redirect(url_for('home'))

    # is_high_speed è un dato booleano, che deriva proprio dal controllo logico che viene fatto a sinistra
    is_high_speed = train[8] == "High-speed"

    # Passo il treno alla bagina booking_form.html
    return render_template('booking_form.html', train_id=train_id, is_high_speed=is_high_speed)

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    # Prendo il tempo corrente
    booking_time = datetime.datetime.now()

    train_id = request.form['train_id']
    user_id = flask_login.current_user.id
    name = request.form['name']
    surname = request.form['surname']
    address = request.form['address']
    city = request.form['city']
    credit_card = request.form['credit_card']
    expire_date_card = request.form['expire_date_card']
    number_of_tickets = int(request.form['number_of_tickets'])
    seat = request.form.get('seat')  # Seat is optional

    # Here you would add the logic to handle the booking, such as saving the booking to a database
    bookings_dao.insert_booking(user_id, train_id, booking_time, name, surname, address, city, credit_card, expire_date_card, number_of_tickets, seat)

    flash(f'Ticket for train {train_id} booked successfully!', 'success')
    return redirect(url_for('home'))

#########################################################
#########################################################
#########################################################
#######First the login and the sign-up page##############
#########################################################
#########################################################
#########################################################
#########################################################

# Define the signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_function():

    # I take from the form the input datas and import them locally as a dictionary
    nuovo_utente_form = request.form.to_dict()

    # I try to retrieve the unique email of the nuovo_utente_form from the db ..
    user_in_db = utenti_dao.get_user_by_email(nuovo_utente_form.get('email'))

    # ... and I check weather it has already been registered ..
    if user_in_db:
        flash('There\'s already a user with these credentials', 'danger')
        return redirect(url_for('signup'))
    # .. and if it hasn't been registered ..
    else:
        # I generate an hash for the password that has been inserted by the form input
        nuovo_utente_form['password'] = ws.generate_password_hash(nuovo_utente_form.get('password'))

        # I add the user to the db using the method "add_user" from the utenti_dao.py
        success = utenti_dao.add_user(nuovo_utente_form)

        if success:
            flash('Utente creato correttamente', 'success')
            return redirect(url_for('home'))
        else:
            flash('Errore nella creazione del utente: riprova!', 'danger')
            return redirect(url_for('signup'))

@login_manager.user_loader
def load_user(user_id):
    db_user = utenti_dao.get_user_by_id(user_id)
    if db_user is not None:
        user = models.User(id=db_user['id'], 
                           email=db_user['email'],
                           password=db_user['password'])
    else:
        user = None
    return user

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():

    # Retrieving the informations from the form @ /login
    utente_form = request.form.to_dict()
    # Using the "get_user_by_nickname" method from utenti.dao, which
    # retrieves the user from the database with the given nickname passed
    # from the form in /login
    utente_db = utenti_dao.get_user_by_email(utente_form['email'])

    # If there's no utente_db in the database (meaning the user just doesn't exist into the db)
    # or if the password given as input in the form /login isn't equal to the one in the database
    if not utente_db or not ws.check_password_hash(utente_db['password'], utente_form['password']):
        flash('Credenziali non valide, riprova', 'danger')
        return redirect(url_for('home'))
    else:
    # if, instead, it exists, we create a new user instance using the "User model" defined in models.py
        # Create a new user instance called "new"
        new = models.User(id=utente_db['id'], 
                          email=utente_db['email'],
                          password=utente_db['password'])
        # We log in said user called "new"
        flask_login.login_user(new, True)
        flash('Bentornato ' + utente_db['email'] + '!', 'success')
        return redirect(url_for('home'))

# Log out route
@app.route("/logout")
@login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')
