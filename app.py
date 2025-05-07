# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class for the web app
app = Flask(__name__)

# Define the route for the homepage ('/')
@app.route('/')
def home():
    # This function returns content for the homepage
    return "Hello, World!"

# Define the route for the 'about' page
@app.route('/about')
def about():
    # This function returns content for the about page
    return "This is the about page"

# Start the Flask development server when the script is run directly
if __name__ == '__main__':
    # Run the app in debug mode (shows helpful error messages)
    app.run(debug=True)
