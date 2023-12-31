from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app = Flask(__name__)

# Configuration for the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/students'

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age =db.Column(db.Integar)
    grade =db.Column(db.String(1))


students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

#http://127.0.0.1:5000/
"http://127.0.0.1:5000/students/"
# @app.route('/students/', methods=['GET'])
def get_students():
        students = Student.query.all()
        fromatted_students = []
        for stud in students:
            fromatted_students.append(
                {
                        "id": stud.id,
                        "first_name": stud.first_name,
                        "last_name": stud.last_name,
                        "age": stud.age,
                        "grade": stud.grade,
                }
            )
        return jsonify(students)


@app.route('/old_students/',  methods=['GET'])
def get_old_students():
        old_students = []
        for index in range(len(students)):
                if students[index]['age'] > 20:
                        old_students.append(students[index])
        return jsonify(old_students)

@app.route('/young_students/', methods=['GET'])
def get_young_students():
        young_students = []
        for index in range(len(students)):
                if students[index]['age'] < 21:
                        young_students.append(students[index])
        return jsonify(young_students)

@app.route('/advance_students/',  methods=['GET'])
def get_advance_students():
        advance_students = []
        for index in range(len(students)):
                if students[index]['age'] < 21 and students[index]['grade'] == 'A':
                        advance_students.append(students[index])
        return jsonify(advance_students)


@app.route('/student_names/', methods=['GET'])
def get_student_names():
        student_names = []
        for index in range(len(students)):
                student_names.append(f"{students[index]['first_name']} {students[index]['last_name']}")
        return jsonify(student_names)

@app.route('/student_ages/', methods=['GET'])
def get_student_ages():
        student_ages = []
        for index in range(len(students)):
                student_name = f"First Name: {students[index]['first_name']} Last Name: {students[index]['last_name']}"
                student_ages.append({student_name: students[index]['age']})
        return jsonify(student_ages)

app.run(debug=True)