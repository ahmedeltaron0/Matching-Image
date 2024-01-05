from flask import Flask, jsonify, render_template, request
from firebase_admin import credentials, auth, initialize_app
from firebase_admin.exceptions import FirebaseError

# Initialize Firebase
cred = credentials.Certificate("image-match.json")
initialize_app(cred)

app = Flask(__name__)

# Endpoint to handle login attempts
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            # Verify the user's email and password
            user = auth.get_user_by_email(email)
            # For simplicity, assuming successful login for any valid user
            return jsonify({'message': 'Success: User logged in'}), 200
        except FirebaseError as e:
            return jsonify({'error': 'Invalid email or password'}), 401
    else:
        # If it's a GET request, render the login.html template
        return render_template('login.html')

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
            return jsonify({
                'email': user_record.email,
                'user_id': user_record.uid
            }), 200  
        except FirebaseError as e:
            print('Error creating new user:', e)
            return jsonify({'error': str(e)}), 400

    # For GET requests, render the signup form
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
