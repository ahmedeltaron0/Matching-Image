import uuid
from flask import Flask, render_template, request, flash, redirect, url_for,jsonify
from firebase_admin import credentials, initialize_app
from firebase_admin import auth  
from firebase_admin.exceptions import FirebaseError
import requests
import os
import base64


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


@app.route('/signin/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            api_key = "AIzaSyCunO6iQEo-nQK0ksMY0HFbiONZMbSafdY"  # Replace with your Firebase API key

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
            return render_template('signin.html')  # Render login page with generic error message

    # For GET requests, render the login form
    return render_template('signin.html')


@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/signin/')
def signin():
    return render_template('signin.html')

@app.route('/about/')
def about():
    return render_template('about.html')



@app.route('/contact/')
def contact():
    return render_template('contact.html')



@app.route('/camera/')
def camera():
    return render_template('camera.html')



@app.route('/ip/')
def ip():
    return render_template('ip.html')



@app.route('/link/')
def link():
    return render_template('link.html')


@app.route('/photo/')
def photo():
    return render_template('photo.html')


@app.route('/home/')
def homeH():
    return render_template('home.html')





@app.route('/save_photo', methods=['POST'])
def save_photo():
    try:
        data = request.get_json()
        photo_data = data.get('photo')

        # Ensure the 'dataset' directory exists
        dataset_directory = 'dataset'
        if not os.path.exists(dataset_directory):
            os.makedirs(dataset_directory)

        # Generate a unique filename for each captured photo
        filename = os.path.join(dataset_directory, f'captured_photo_{uuid.uuid4()}.jpg')

        # Decode base64 data and save the photo
        with open(filename, 'wb') as file:
            file.write(base64.b64decode(photo_data.split(',')[1]))

        return jsonify({'message': 'Photo saved successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
    



if __name__ == '__main__':
    app.run(debug=True)
