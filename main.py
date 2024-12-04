from student import Student
from flask import Flask

app = Flask(__name__)
list_of_students = []
angela = Student("Angela", 1)
tom = Student("Tom", 2)
list_of_students.append(angela)
list_of_students.append(tom)

@app.route("/<name>/<int:id>")
def create_student(name, id):
    student = Student(name, id)
    list_of_students.append(student)
    return f"Student {student.name} have been created with ID {student.id}"


@app.route("/")
def print_list():
    s = ''
    for student in list_of_students:
        s = s + f"{student.name} with {student.id}<br>"
    return s


@app.route("/update/<id>/<new_name>")
def update_student_name(id, new_name):
    for student in list_of_students:
        if student.id == int(id):
            student.name = new_name
            return f"Student\'s name has been changed to {student.name}"
    return "Student not found"


@app.route("/delete/<int:id>")
def delete_student(id):
    for student in list_of_students:
        if student.id == id:
            list_of_students.remove(student)
            return f"Student {student.name} has been deleted"
    return "Student not found"


if __name__ == "__main__":
    app.run(debug=True)

