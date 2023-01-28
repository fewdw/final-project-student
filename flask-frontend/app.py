from flask import Flask, render_template,redirect,request,jsonify,session
from flask_session import Session
import requests, json
import bcrypt
import ast

from student_api_request import get_all_students_from_api, get_one_student_from_api, delete_student_from_api,edited_student_admin_api_request, add_student_to_list
from degree_api_request import get_all_degrees_from_api, delete_degree_from_api,post_a_degree_to_api, put_a_degree_to_api
from project_api_request import get_all_projects_from_api, delete_project_from_api, post_a_project_to_api, put_a_project_to_api
from credential_api_request import get_credentials_from_api, post_credentials_from_api, put_credentials_from_api, delete_credentials_from_api, get_credentials_by_id_from_api

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

with open('i18n.json', encoding='utf-8') as f:
    i18n = json.load(f)

# login routes
@app.route('/')
def employer_index():
    if session.get("type") == "employer":
        return redirect("/employer/list")

    if session.get("type") == "staff":
        return redirect("/staff/list")

    if session.get("type") == "admin":
        return redirect("/admin/list")

    return render_template("logins/employer-login.html", I18N=i18n, LANG=session.get("lang"))


@app.route('/admin')
def admin_index():
    if session.get("type") == "employer":
        return redirect("/employer/list")

    if session.get("type") == "staff":
        return redirect("/staff/list")

    if session.get("type") == "admin":
        return redirect("/admin/list")

    return render_template("logins/admin-login.html", I18N=i18n, LANG=session.get("lang"))


@app.route('/staff')
def staff_index():
    if session.get("type") == "employer":
        return redirect("/employer/list")
        
    if session.get("type") == "staff":
        return redirect("/staff/list")

    if session.get("type") == "admin":
        return redirect("/admin/list")
        
    return render_template("logins/staff-login.html", I18N=i18n, LANG=session.get("lang"))


# list routes
@app.route('/employer/list')
def employer_list_home():
    if session.get("type") == "employer":
        return render_template("list/employer-list-admin.html", STUDENTS = get_all_students_from_api(), I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"))
    return redirect("/")


@app.route('/staff/list')
def staff_list_home():
    if session.get("type") == "staff":
        return render_template("list/staff-list-admin.html", STUDENTS = get_all_students_from_api(), I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"))
    return redirect("/staff")


@app.route('/admin/list')
def admin_list_home():
    if session.get("type") == "admin":
        return render_template("list/admin-list-admin.html", STUDENTS = get_all_students_from_api(), I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"))
    return redirect("/admin")

# routing for student by specific fields
@app.route('/teacher/<professor_name>')
def admin_list_teacher(professor_name):
    if session.get("type") == "admin":
        filter_student_by_teacher = []
        all_students = get_all_students_from_api()
        for i in all_students: 
            if i["professor_name"] == professor_name:
                filter_student_by_teacher.append(i)
        return render_template("list/admin-list-admin.html", STUDENTS = filter_student_by_teacher, I18N=i18n, LANG=session.get("lang"))
    return redirect("/admin")

# more info route
@app.route('/admin/list/student/id/<id>')
def admin_more_info(id):
    if session.get("type") == "admin":
        return render_template('moreinfo/student-more-info-admin.html', STUDENT = get_one_student_from_api(id), I18N=i18n, LANG=session.get("lang"))
    return redirect("/admin")


@app.route('/employer/list/student/id/<id>')
def employer_more_info(id):
    if session.get("type") == "employer":
        return render_template('moreinfo/student-more-info-employer.html', STUDENT = get_one_student_from_api(id), I18N=i18n, LANG=session.get("lang"))
    return redirect("/")


@app.route('/staff/list/student/id/<id>')
def staff_more_info(id):
    if session.get("type") == "staff":
        return render_template('moreinfo/student-more-info-staff.html', STUDENT = get_one_student_from_api(id), I18N=i18n, LANG=session.get("lang"))
    return redirect("/staff")


# delete route
@app.route("/admin/list/student/id/delete/<id>")
def admin_delete_student(id):
    if session.get("type") == "admin":
        delete_student_from_api(id)
        return redirect("/admin/list")
    return redirect("/admin")


# add student
@app.route("/student/addstudent")
def add_student_admin():
    if session.get("type") == "admin":
        return render_template("addstudent/add-student-admin.html", DEGREES=get_all_degrees_from_api(), PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/admin")







@app.route("/staff/list/student/addstudent")
def add_student_staff():
    if session.get("type") == "staff":
        return render_template("addstudent/add-student-staff.html", DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/staff")

@app.route("/admin/list/student/editstudent/<id>")
def edit_student_admin(id):
    if session.get("type") == "admin":
        return render_template("editstudent/edit-student-admin.html", STUDENT = get_one_student_from_api(id),DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/")

@app.route("/staff/list/student/editstudent/<id>")
def edit_student_staff(id):
    if session.get("type") == "staff":
        return render_template("editstudent/edit-student-staff.html", STUDENT = get_one_student_from_api(id),DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/staff")


@app.route("/admin/list/studentUpdated/", methods=["POST"])
def edited_student_admin():
    if request.method == "POST" and session.get("type") == "admin":
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
    return redirect("/")

@app.route("/staff/list/studentUpdated/", methods=["POST"])
def edited_student_staff():
    if request.method == "POST" and session.get("type") == "staff":
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
    return redirect("/")
    
@app.route("/staff/list/student/studentadded",methods=["POST"])
def student_added_from_form_staff():
    if request.method == "POST" and session.get("type") == "staff":
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
    return redirect("/")

@app.route("/admin/list/student/studentadded",methods=["POST"])
def student_added_from_form_admin():
    if request.method == "POST" and session.get("type") == "admin":
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
    return redirect("/")

@app.route("/admin/pannel")
def admin_pannel():
    if session.get("type") == "admin":
        return render_template("admin-project-degree-pannel.html",DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), CREDENTIALS=get_credentials_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/admin")

@app.route("/staff/pannel")
def staff_pannel():
    if session.get("type") == "staff":
        return render_template("staff-project-degree-pannel.html",DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/staff")

@app.route("/admin/pannel/deletedegree",methods=["POST"])
def delete_a_degree_by_id_route():
    if request.method == "POST" and session.get("type") == "admin":
        delete_degree_from_api(request.form.get("id"))
        return redirect("/admin/pannel")
    return redirect("/")

@app.route("/admin/pannel/adddegree",methods=["POST"])
def post_a_degree_route():
    if request.method == "POST" and session.get("type") == "admin":
        post_a_degree_to_api(
            request.form.get("degree_id"),
            request.form.get("name_degree"),
            request.form.get("description")
        )
        return redirect("/admin/pannel")
    return redirect("/")

@app.route("/staff/pannel/deletedegree",methods=["POST"])
def delete_a_degree_by_id_staff_route():
    if request.method == "POST" and session.get("type") == "staff":
        delete_degree_from_api(request.form.get("id"))
        return redirect("/staff/pannel")
    return redirect("/")

@app.route("/staff/pannel/adddegree",methods=["POST"])
def post_a_degree_staff_route():
    if request.method == "POST" and session.get("type") == "staff":
        post_a_degree_to_api(
            request.form.get("degree_id"),
            request.form.get("name_degree"),
            request.form.get("description")
        )
        return redirect("/staff/pannel")
    return redirect("/")

@app.route("/admin/pannel/deleteproject",methods=["POST"])
def delete_a_project_by_id_route():
    if request.method == "POST" and session.get("type") == "admin":
        delete_project_from_api(request.form.get("id"))
        return redirect("/admin/pannel")
    return redirect("/")

@app.route("/admin/pannel/addproject",methods=["POST"])
def post_a_project_route():
    if request.method == "POST" and session.get("type") == "admin":
        post_a_project_to_api(
            request.form.get("project_id"),
            request.form.get("project_name"),
            request.form.get("project_description")
        )
        return redirect("/admin/pannel")
    return redirect("/")

@app.route("/staff/pannel/deleteproject",methods=["POST"])
def delete_a_project_by_id_route_staff():
    if request.method == "POST" and session.get("type") == "staff":
        delete_project_from_api(request.form.get("project_id"))
        return redirect("/staff/pannel")
    return redirect("/")

@app.route("/staff/pannel/addproject",methods=["POST"])
def post_a_project_route_staff():
    if request.method == "POST" and session.get("type") == "staff":
        post_a_project_to_api(
            request.form.get("project_id"),
            request.form.get("project_name"),
            request.form.get("project_description")
        )
        return redirect("/staff/pannel")

@app.route("/admin/pannel/updatedegree",methods=["POST"])
def update_a_degree_route_admin():
    if request.method == "POST" and session.get("type") == "admin":
        put_a_degree_to_api(
            request.form.get("id"),
            request.form.get("degree_id"),
            request.form.get("name_degree"),
            request.form.get("description")
        )
        return redirect("/admin/pannel")
    return redirect("/")

@app.route("/admin/pannel/updateproject",methods=["POST"])
def update_a_project_route_admin():
    if request.method == "POST" and session.get("type") == "admin":
        put_a_project_to_api(
            request.form.get("id"),
            request.form.get("project_id"),
            request.form.get("name_project"),
            request.form.get("description")
        )
        return redirect("/admin/pannel")
    return redirect("/")


@app.route("/admin/credentials/deletecredential", methods=["POST"])
def delete_a_credential_route():
    if request.method == "POST" and session.get("type") == "admin":
        delete_credentials_from_api(request.form.get("id"))
        return redirect("/admin/pannel")
    return redirect("/")

@app.route("/admin/credentials/addcredential", methods=["POST"])
def add_credential_route():
    if request.method == "POST" and session.get("type") == "admin":
        email = request.form.get("email")
        password = request.form.get("password")
        lang = request.form.get("lang")
        session_type = request.form.get("type")

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

        post_credentials_from_api(email,hashed_pw,lang,session_type)

        return redirect("/admin/pannel")
    return redirect("/")

@app.route("/admin/login", methods=["POST"])
def validate_admin_login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return redirect("/admin")
    
    credentials = get_credentials_from_api()

    for obj in credentials:
        if obj["email"] == email and obj["type"] == "admin":
            if bcrypt.checkpw(password.encode('utf-8'), obj["hash"].encode('utf-8')):
                #CREATE SESSION!
                session["name"] = obj["email"]
                session["lang"] = obj["lang"]
                session["type"] = obj["type"]
                return redirect("/admin/list")
    return redirect("/admin")

@app.route("/staff/login", methods=["POST"])
def validate_staff_login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return redirect("/staff")
    
    credentials = get_credentials_from_api()

    for obj in credentials:
        if obj["email"] == email and obj["type"] == "staff":
            if bcrypt.checkpw(password.encode('utf-8'), obj["hash"].encode('utf-8')):
                #CREATE SESSION!
                session["name"] = obj["email"]
                session["lang"] = obj["lang"]
                session["type"] = obj["type"]
                return redirect("/staff/list")
    return redirect("/staff")

@app.route("/employer/login", methods=["POST"])
def validate_employer_login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return redirect("/")
    
    credentials = get_credentials_from_api()

    for obj in credentials:
        if obj["email"] == email and obj["type"] == "employer":
            if bcrypt.checkpw(password.encode('utf-8'), obj["hash"].encode('utf-8')):
                #CREATE SESSION!
                session["name"] = obj["email"]
                session["lang"] = obj["lang"]
                session["type"] = obj["type"]
                return redirect("/employer/list")
    return redirect("/")

@app.route("/clearsession")
def clear_session():
    session["name"] = None
    session["lang"] = None
    session["type"] = None
    return redirect("/")

@app.route("/test")
def test():
    return jsonify({"name": session["name"], "lang": session["lang"], "type": session["type"]})

@app.route("/admin/changelang", methods=["POST"])
def admin_changelang_route():
    if request.method == "POST" and session.get("type") == "admin":
        lang = request.form.get("lang")
        email = request.form.get("email")

        credentials = get_credentials_from_api()

        for obj in credentials:
            if obj["email"] == email:
                put_credentials_from_api(
                    obj["_id"]["$oid"],
                    obj["email"],
                    obj["hash"],
                    lang,
                    obj["type"]
                )
                session["lang"] = lang
                return redirect("/admin/list")
        return redirect("/admin/list")
    return redirect("/")

@app.route("/employer/changelang", methods=["POST"])
def employer_changelang_route():
    if request.method == "POST" and session.get("type") == "employer":
        lang = request.form.get("lang")
        email = request.form.get("email")

        credentials = get_credentials_from_api()

        for obj in credentials:
            if obj["email"] == email:
                put_credentials_from_api(
                    obj["_id"]["$oid"],
                    obj["email"],
                    obj["hash"],
                    lang,
                    obj["type"]
                )
                session["lang"] = lang
                return redirect("/admin/list")
        return redirect("/admin/list")
    return redirect("/")

@app.route("/staff/changelang", methods=["POST"])
def staff_changelang_route():
    if request.method == "POST" and session.get("type") == "admin":
        lang = request.form.get("lang")
        email = request.form.get("email")

        credentials = get_credentials_from_api()

        for obj in credentials:
            if obj["email"] == email:
                put_credentials_from_api(
                    obj["_id"]["$oid"],
                    obj["email"],
                    obj["hash"],
                    lang,
                    obj["type"]
                )
                session["lang"] = lang
                return redirect("/admin/list")
        return redirect("/admin/list")
    return redirect("/")

@app.route("/admin/archive", methods=["POST"])
def archive_student_route():
    if request.method == "POST" and session.get("type") == "admin":
        delete_student_from_api(request.form.get("_id"))
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
            request.form.get("programming_language"),
            status=request.form.get("status")
        )
        return redirect('/admin/list')
    return redirect("/")

@app.route("/staff/archive", methods=["POST"])
def archive_student_route_staff():
    if request.method == "POST" and session.get("type") == "staff":
        delete_student_from_api(request.form.get("_id"))
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
            request.form.get("programming_language"),
            status=request.form.get("status")
        )
        return redirect('/staff/list')
    return redirect("/")

@app.route("/admin/filter", methods=["POST"])
def adminFilterRoute():
    filteredStudents = []
    Technologies = request.form.get("Technologies").strip()
    list = Technologies.split(" ")
    students=get_all_students_from_api()
    for s in students:
        for t in list:
            if t in s["programming_language"]:
               filteredStudents.append(s)
    return render_template("list/filtered-admin-list.html", STUDENTS = filteredStudents, I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"))

if __name__ == '__main__':
    app.run()