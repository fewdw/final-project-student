from flask import Flask, render_template,redirect,request
import requests, json

from student_api_request import get_all_students_from_api, get_one_student_from_api, delete_student_from_api,edited_student_admin_api_request, add_student_to_list
from degree_api_request import get_all_degrees_from_api, delete_degree_from_api,post_a_degree_to_api, put_a_degree_to_api
from project_api_request import get_all_projects_from_api, delete_project_from_api, post_a_project_to_api, put

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


# routing for student by specific fields

@app.route('/teacher/<professor_name>')
def admin_list_teacher(professor_name):
    filter_student_by_teacher = []
    all_students = get_all_students_from_api()
    for i in all_students: 
        if i["professor_name"] == professor_name:
            filter_student_by_teacher.append(i)
    return render_template("list/admin-list-admin.html", STUDENTS = filter_student_by_teacher)

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
    return render_template("addstudent/add-student-admin.html", DEGREES=get_all_degrees_from_api(), PROJECTS = get_all_projects_from_api())


@app.route("/staff/list/student/addstudent")
def add_student_staff():
    return render_template("addstudent/add-student-staff.html", DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api())

@app.route("/admin/list/student/editstudent/<id>")
def edit_student_admin(id):
    return render_template("editstudent/edit-student-admin.html", STUDENT = get_one_student_from_api(id),DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api())

@app.route("/staff/list/student/editstudent/<id>")
def edit_student_staff(id):
    return render_template("editstudent/edit-student-staff.html", STUDENT = get_one_student_from_api(id),DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api())

@app.route("/admin/list/studentUpdated/", methods=["POST"])
def edited_student_admin():
    delete_student_from_api(request.form.get("id"))
    add_student_to_list(
        request.form.get("student_id"),
        request.form.get("first_name"),
        request.form.get("last_name"),
        request.form.get("email"),
        request.form.get("gender"),
        request.form.get("professor_name"),
        request.form.get("year_of_graduation"),
        request.form.get("degree"),
        request.form.get("projectId"),
        request.form.get("programming_language")
    )
    return redirect ("/admin/list")

@app.route("/staff/list/studentUpdated/", methods=["POST"])
def edited_student_staff():
    delete_student_from_api(request.form.get("id"))
    add_student_to_list(
        request.form.get("student_id"),
        request.form.get("first_name"),
        request.form.get("last_name"),
        request.form.get("email"),
        request.form.get("gender"),
        request.form.get("professor_name"),
        request.form.get("year_of_graduation"),
        request.form.get("degree"),
        request.form.get("projectId"),
        request.form.get("programming_language")
    )
    return redirect ("/staff/list")
    
    
@app.route("/staff/list/student/studentadded",methods=["POST"])
def student_added_from_form_staff():

    #call function to post to student api
    add_student_to_list(
    request.form.get("student_Id"),
    request.form.get("first_name"),
    request.form.get("last_name"),
    request.form.get("email"),
    request.form.get("gender"),
    request.form.get("professor_name"),
    request.form.get("year_of_graduation"),
    request.form.get("degree"),
    request.form.get("projectId"),
    request.form.get("programming_language")
    )
    return redirect("/staff/list")
@app.route("/admin/list/student/studentadded",methods=["POST"])
def student_added_from_form_admin():
    #call function to post to student api
    add_student_to_list(
    request.form.get("student_Id"),
    request.form.get("first_name"),
    request.form.get("last_name"),
    request.form.get("email"),
    request.form.get("gender"),
    request.form.get("professor_name"),
    request.form.get("year_of_graduation"),
    request.form.get("degree"),
    request.form.get("projectId"),
    request.form.get("programming_language")
    )
    return redirect("/admin/list")

@app.route("/admin/pannel")
def admin_pannel():
    return render_template("admin-project-degree-pannel.html",DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api())

@app.route("/staff/pannel")
def staff_pannel():
    return render_template("staff-project-degree-pannel.html",DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api())

@app.route("/admin/pannel/deletedegree",methods=["POST"])
def delete_a_degree_by_id_route():
    delete_degree_from_api(request.form.get("id"))
    return redirect("/admin/pannel")

@app.route("/admin/pannel/adddegree",methods=["POST"])
def post_a_degree_route():
    post_a_degree_to_api(
        request.form.get("degree_id"),
        request.form.get("name_degree"),
        request.form.get("description")
    )
    return redirect("/admin/pannel")

@app.route("/staff/pannel/deletedegree",methods=["POST"])
def delete_a_degree_by_id_staff_route():
    delete_degree_from_api(request.form.get("id"))
    return redirect("/staff/pannel")

@app.route("/staff/pannel/adddegree",methods=["POST"])
def post_a_degree_staff_route():
    post_a_degree_to_api(
        request.form.get("degree_id"),
        request.form.get("name_degree"),
        request.form.get("description")
    )
    return redirect("/staff/pannel")

##
@app.route("/admin/pannel/deleteproject",methods=["POST"])
def delete_a_project_by_id_route():
    delete_project_from_api(request.form.get("project_id"))
    return redirect("/admin/pannel")

@app.route("/admin/pannel/addproject",methods=["POST"])
def post_a_project_route():
    post_a_project_to_api(
        request.form.get("project_id"),
        request.form.get("project_name"),
        request.form.get("project_description")
    )
    return redirect("/admin/pannel")

@app.route("/staff/pannel/deleteproject",methods=["POST"])
def delete_a_project_by_id_route_staff():
    delete_project_from_api(request.form.get("project_id"))
    return redirect("/staff/pannel")

@app.route("/staff/pannel/addproject",methods=["POST"])
def post_a_project_route_staff():
    post_a_project_to_api(
        request.form.get("project_id"),
        request.form.get("project_name"),
        request.form.get("project_description")
    )
    return redirect("/staff/pannel")

@app.route("/admin/pannel/updatedegree",methods=["POST"])
def update_a_degree_route_admin():
    put_a_degree_to_api(
        request.form.get("id"),
        request.form.get("degree_id"),
        request.form.get("name_degree"),
        request.form.get("description")
    )
    return redirect("/admin/pannel")

if __name__ == '__main__':
    app.run()