from flask import Flask, render_template
import requests, json

app = Flask(__name__)

student_list = "http://127.0.0.1:5000/students/"

# get all students
response = requests.get(student_list)
students = json.loads(response.text)

# login routes
@app.route('/')
def employer_index():
    return render_template("logins/employer-login.html")


@app.route('/admin')
def admin_index():
    return render_template("logins/admin-login.html")


@app.route('/staff')
def staff_index():
    return render_template("logins/staff-login.html")


# list routes
@app.route('/employer/list')
def employer_list_home():
    return render_template("list/employer-list-admin.html", STUDENTS = students)


@app.route('/staff/list')
def staff_list_home():
    return render_template("list/staff-list-admin.html", STUDENTS = students)


@app.route('/admin/list')
def admin_list_home():
    return render_template("list/admin-list-admin.html", STUDENTS = students)


if __name__ == '__main__':
    app.run()

