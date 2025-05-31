#  Hello guys today i write database program.
#  and with help of flask and python we can use this program to connect the webpage to any database

from flask import Flask, request, redirect, render_template # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLite database URI and disable modification tracking for performance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object with the app
db = SQLAlchemy(app)

# Define the Student model/table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each student
    name = db.Column(db.String(100))              # Student's name
    age = db.Column(db.Integer)                   # Student's age
    email = db.Column(db.String(100))             # Student's email

    def __repr__(self):
        return f"<Student {self.name}, Email: {self.email}>"

# Create all tables defined with SQLAlchemy if they don't exist
with app.app_context():
    db.create_all()

# Route to show the form to add a new student
@app.route("/")
def home():
    return render_template("add_Student.html")

# Route to handle form submission and add new student to the database
@app.route("/add_Student", methods=["POST"])
def add():
    # Get form data from the request
    name = request.form.get("name")
    age = request.form.get("age")
    email = request.form.get("email")

    # Create a new Student object and add it to the database
    new_student = Student(name=name, age=int(age), email=email)
    db.session.add(new_student)
    db.session.commit()

    return f"Student Name: {name} and Email: {email} added successfully!"

# Route to display form for editing an existing student using their ID
@app.route("/edit/<int:id>")
def edit_student(id):
    # Get student by ID or return 404 if not found
    student = Student.query.get_or_404(id)
    return render_template("edit_Student.html", student=student)

# Route to handle the form submission for updating a student's data
@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    # Get student by ID or return 404 if not found
    student = Student.query.get_or_404(id)

    # Update student fields with new data from form
    student.name = request.form['name']
    student.age = request.form['age']
    student.email = request.form['email']

    # Save the updated data to the database
    db.session.commit()
    return f"Student ID {id} updated successfully!"

# Route to display all students in a list
@app.route("/data_Student")
def list_students():
    # Fetch all students from the database
    students = Student.query.all()
    return render_template("list_students.html", students=students)

# Run the app only if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
