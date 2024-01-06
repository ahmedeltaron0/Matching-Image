from flask import Flask, render_template, request, flash, redirect, url_for
from firebase_admin import credentials, initialize_app
from firebase_admin import auth  # Import auth after initialize_app
from firebase_admin.exceptions import FirebaseError

# Initialize Firebase
cred = credentials.Certificate("image-match.json")
initialize_app(cred)

app = Flask(__name__)
app.secret_key = 'qwertyuiopasdfg'

# Endpoint to render signup page and handle user registration
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user_record = auth.create_user(
                email=email,
                password=password
            )
            print('Successfully created new user:', user_record.uid)

            # Redirect to login page on successful signup
            return redirect(url_for('login'))

        except FirebaseError as e:
            print('Error creating new user:', e)

            # Pass error message to signup.html
            return render_template('signup.html', error_message="Failed signup")

    # For GET requests, render the signup form
    return render_template('signup.html')

# Endpoint to render login page and handle user login
import requests

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            api_key = "YOUR_API_KEY"  # Replace with your Firebase API key

            # Sign in using email and password through Firebase Authentication REST API
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True
            }

            response = requests.post(url, json=payload)

            if response.ok:
                user_data = response.json()
                # Successfully logged in, handle the user data as needed
                # For example, you might want to retrieve the user's ID token
                user_id_token = user_data['idToken']
                flash('Success: User logged in', 'success')
                return redirect('/')  # Redirect to home page after successful login
            else:
                # Handle login failure, get error message from Firebase
                error_message = response.json().get('error', {}).get('message', 'Invalid email or password')
                flash(error_message, 'error')
                return render_template('login.html')  # Render login page with error message

        except Exception as e:
            flash('Login failed', 'error')
            return render_template('login.html')  # Render login page with generic error message

    # For GET requests, render the login form
    return render_template('login.html')


@app.route('/')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
