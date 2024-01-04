from flask import Flask, render_template, request, redirect, url_for
from firebase_admin import credentials, auth
import firebase_admin



cred = credentials.Certificate("image-match.json")
firebase_admin.initialize_app(cred)



app = Flask(__name__)

@app.route('/')
def host():
    return "Home"

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.get_user_by_email(email)
            # If no exception is raised, user exists in Firebase
            auth_user = auth.update_user(user.uid, password=password)  # Attempt to update password
            return 'Success'  # Modify this to render a success page or message
        except auth.AuthError as e:
            # If user does not exist or password update fails
            print(e)  # Log the error (for demonstration purposes)
            return redirect(url_for('host'))  # Redirect to home page if login fails

    # If the request method is GET (when the user navigates to the login page)
    return render_template('login.html')  # Render the login page

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Process signup data (e.g., save to database)
        return f"Received signup request for {email}"
    else:
        return render_template('signup.html')  # Render the signup form

if __name__ == "__main__":
    app.run(debug=True)
