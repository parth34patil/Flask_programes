from flask import Flask, render_template, request  # Import necessary Flask modules

app = Flask(__name__)  # Create an instance of the Flask application


# Route for the home page
@app.route('/')
def hello():
    # Render the 'home.html' template when the root URL is accessed
    return render_template('home.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def login():
    # Get form data submitted from 'home.html'
    name = request.form.get('name')       # Get the value of 'name' from the form
    email = request.form.get('email')     # Get the value of 'email' from the form
    password = request.form.get('password')  # Get the value of 'password' from the form

    # Return a response string using the submitted form data
    return f'welcome to study_stream {name} and thanks to provide your email id {email} and this is your password = {password}'


# Route to render another page
@app.route('/after')
def after():
    # Render the 'base.html' template when '/after' URL is accessed
    return render_template('base.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
