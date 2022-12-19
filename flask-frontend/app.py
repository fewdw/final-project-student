from flask import Flask, render_template,redirect, request
import requests, json

from student_api_request import get_all_students_from_api, get_one_student_from_api, delete_student_from_api

app = Flask(__name__)

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
    return render_template("list/employer-list-admin.html", STUDENTS = get_all_students_from_api())


@app.route('/staff/list')
def staff_list_home():
    return render_template("list/staff-list-admin.html", STUDENTS = get_all_students_from_api())


@app.route('/admin/list')
def admin_list_home():
    return render_template("list/admin-list-admin.html", STUDENTS = get_all_students_from_api())


# more info route
@app.route('/admin/list/student/id/<id>')
def admin_more_info(id):
    return render_template('moreinfo/student-more-info-admin.html', STUDENT = get_one_student_from_api(id))


@app.route('/employer/list/student/id/<id>')
def employer_more_info(id):
    return render_template('moreinfo/student-more-info-employer.html', STUDENT = get_one_student_from_api(id))


@app.route('/staff/list/student/id/<id>')
def staff_more_info(id):
    return render_template('moreinfo/student-more-info-staff.html', STUDENT = get_one_student_from_api(id))


# delete route
@app.route("/admin/list/student/id/delete/<id>")
def admin_delete_student(id):
    delete_student_from_api(id)
    return redirect("/admin/list")


# add student
@app.route("/admin/list/student/addstudent")
def add_student_admin():
    return render_template("addstudent/add-student-admin.html")


@app.route("/staff/list/student/addstudent")
def add_student_staff():
    return render_template("addstudent/add-student-staff.html")


@app.route("/admin/list/student/studentadded",methods=["POST"])
def student_added_from_form():
    request.form.get("student_Id")
    request.form.get("Status: True")
    request.form.get("first_name")
    request.form.get("last_name")
    request.form.get("email")
    request.form.get("gender")
    request.form.get("professor_name")
    request.form.get("year_of_graduation")
    request.form.get("degree")
    request.form.get("projectId")
    request.form.get("programming_language")

    #call function to post to student api
    # redirect to /admin/list
    return 


if __name__ == '__main__':
    app.run()

