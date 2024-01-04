from flask import Flask, jsonify, render_template, request, redirect, url_for
from firebase_admin import credentials, auth, initialize_app
from firebase_admin.exceptions import FirebaseError  # Import FirebaseError for handling exceptions
import firebase_admin




cred = credentials.Certificate("image-match.json")
firebase_admin.initialize_app(cred)



app = Flask(__name__)

@app.route('/')
def host():
    return "Home"
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']

    try:
       # Verify the user's email and password
        user = auth.get_user_by_email(email)
        token = auth.create_custom_token(user.uid)
        return jsonify({'token': token.decode()}), 200
    except firebase_admin.auth.AuthError:
        return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/signup', methods=['GET', 'POST'])
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
            # json that has the user id and the email
            return jsonify({
                'email': user_record.email,
                'user_id': user_record.uid
            }), 200  
        except FirebaseError as e:
            # Handle Firebase errors
            print('Error creating new user:', e)
            return jsonify({'error': str(e)}), 400 # Or render a template with the error

    # Render the signup form for GET requests
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
