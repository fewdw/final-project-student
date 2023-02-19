from flask import Flask, render_template,redirect,request,jsonify,session,make_response
from flask_session import Session
import requests, json
import bcrypt
import ast
import base64

from student_api_request import get_all_students_from_api, get_one_student_from_api, delete_student_from_api,edited_student_admin_api_request, add_student_to_list
from degree_api_request import get_all_degrees_from_api, delete_degree_from_api,post_a_degree_to_api, put_a_degree_to_api
from project_api_request import get_all_projects_from_api, delete_project_from_api, post_a_project_to_api, put_a_project_to_api
from credential_api_request import get_credentials_from_api, post_credentials_from_api, put_credentials_from_api, delete_credentials_from_api, get_credentials_by_id_from_api
from emailer import send_mail

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


# list routes
@app.route('/employer/list')
def employer_list_home():
    if session.get("type") == "employer":
        return render_template("list/employer-list-admin.html", STUDENTS = get_all_students_from_api(), I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"), DEGREES=get_all_degrees_from_api(), PROJECTS=get_all_projects_from_api())
    return redirect("/")


@app.route('/staff/list')
def staff_list_home():
    if session.get("type") == "staff":
        return render_template("list/staff-list-admin.html", STUDENTS = get_all_students_from_api(), I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"), DEGREES=get_all_degrees_from_api(),  PROJECTS=get_all_projects_from_api())
    return redirect("/staff")


@app.route('/admin/list')
def admin_list_home():
    if session.get("type") == "admin":
        #[0:2]
        return render_template("list/admin-list-admin.html", STUDENTS = get_all_students_from_api(), I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"), DEGREES=get_all_degrees_from_api(), PROJECTS=get_all_projects_from_api())
    return redirect("/")

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
    return redirect("/")

# more info route
@app.route('/admin/list/student/id/<id>')
def admin_more_info(id):
    if session.get("type") == "admin":

        student = get_one_student_from_api(id)
        projects = get_all_projects_from_api()

        matching_project = next((p for p in projects if p["project_name"] == student["projectId"]), None)

        if matching_project:
            description = matching_project["project_description"]
        else:
            description = "project has no description yet"

        return render_template('moreinfo/student-more-info-admin.html', STUDENT = student, DESCRIPTION=description, I18N=i18n, LANG=session.get("lang"))
    return redirect("/")


@app.route('/employer/list/student/id/<id>')
def employer_more_info(id):
    if session.get("type") == "employer":

        student = get_one_student_from_api(id)
        projects = get_all_projects_from_api()

        matching_project = next((p for p in projects if p["project_name"] == student["projectId"]), None)

        if matching_project:
            description = matching_project["project_description"]
        else:
            description = "project has no description yet"

        return render_template('moreinfo/student-more-info-employer.html', STUDENT = student, DESCRIPTION=description, I18N=i18n, LANG=session.get("lang"))
    return redirect("/")


@app.route('/staff/list/student/id/<id>')
def staff_more_info(id):
    if session.get("type") == "staff":

        student = get_one_student_from_api(id)
        projects = get_all_projects_from_api()

        matching_project = next((p for p in projects if p["project_name"] == student["projectId"]), None)

        if matching_project:
            description = matching_project["project_description"]
        else:
            description = "project has no description yet"

        return render_template('moreinfo/student-more-info-staff.html', STUDENT = student, DESCRIPTION=description, I18N=i18n, LANG=session.get("lang"))
    return redirect("/")


# delete route
@app.route("/admin/list/student/id/delete/<id>")
def admin_delete_student(id):
    if session.get("type") == "admin":
        delete_student_from_api(id)
        return redirect("/admin/list")
    return redirect("/")


# add student
@app.route("/student/addstudent")
def add_student_admin():
    if session.get("type") == "admin":
        return render_template("addstudent/add-student-admin.html", DEGREES=get_all_degrees_from_api(), PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/")


@app.route("/staff/list/student/addstudent")
def add_student_staff():
    if session.get("type") == "staff":
        return render_template("addstudent/add-student-staff.html", DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/")

@app.route("/admin/list/student/editstudent/<id>")
def edit_student_admin(id):
    if session.get("type") == "admin":
        return render_template("editstudent/edit-student-admin.html", STUDENT = get_one_student_from_api(id),DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/")

@app.route("/staff/list/student/editstudent/<id>")
def edit_student_staff(id):
    if session.get("type") == "staff":
        return render_template("editstudent/edit-student-staff.html", STUDENT = get_one_student_from_api(id),DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/")


@app.route("/admin/list/studentUpdated/", methods=["POST"])
def edited_student_admin():
    if request.method == "POST" and session.get("type") == "admin":

        old_pdf = request.form.get("old_pdf_string")
        pdf_file = request.files.get("pdf_file")
        pdf_data = pdf_file.read()
        pdf_data_b64 = base64.b64encode(pdf_data).decode('utf-8')

        if len(pdf_data_b64) == 0:
            #olf pdf
            pdf_to_post = old_pdf
        else:
            #new pdf
            pdf_to_post = pdf_data_b64


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
            request.form.get("programming_language"),
            pdf_to_post
        )
        return redirect ("/admin/list")
    return redirect("/")

@app.route("/staff/list/studentUpdated/", methods=["POST"])
def edited_student_staff():
    if request.method == "POST" and session.get("type") == "staff":

        old_pdf = request.form.get("old_pdf_string")
        pdf_file = request.files.get("pdf_file")
        pdf_data = pdf_file.read()
        pdf_data_b64 = base64.b64encode(pdf_data).decode('utf-8')

        if len(pdf_data_b64) == 0:
            #olf pdf
            pdf_to_post = old_pdf
        else:
            #new pdf
            pdf_to_post = pdf_data_b64


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
            request.form.get("programming_language"),
            pdf_to_post
        )
        return redirect ("/staff/list")
    return redirect("/")
    
@app.route("/staff/list/student/studentadded",methods=["POST"])
def student_added_from_form_staff():

    pdf_file = request.files.get("pdf_file")
    pdf_data = pdf_file.read()
    pdf_data_b64 = base64.b64encode(pdf_data).decode('utf-8')

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
        request.form.get("programming_language"),
        pdf_data_b64
        )
        return redirect("/staff/list")
    return redirect("/")

@app.route("/admin/list/student/studentadded",methods=["POST"])
def student_added_from_form_admin():

    pdf_file = request.files.get("pdf_file")
    pdf_data = pdf_file.read()
    pdf_data_b64 = base64.b64encode(pdf_data).decode('utf-8')

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
        request.form.get("programming_language"),
        pdf_data_b64
        )
        return redirect("/admin/list")
    return redirect("/")

@app.route("/admin/pannel")
def admin_pannel():
    if session.get("type") == "admin":
        return render_template("admin-project-degree-pannel.html",DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), CREDENTIALS=get_credentials_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/")

@app.route("/staff/pannel")
def staff_pannel():
    if session.get("type") == "staff":
        return render_template("staff-project-degree-pannel.html",DEGREES=get_all_degrees_from_api(),PROJECTS = get_all_projects_from_api(), I18N=i18n, LANG=session.get("lang"))
    return redirect("/")

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
        print(request.form.get("degree_id"))
        delete_degree_from_api(request.form.get("degree_id"))
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
            request.form.get("name_project"),
            request.form.get("description")
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
            request.form.get("name_project"),
            request.form.get("description")
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

@app.route("/staff/pannel/updatedegree",methods=["POST"])
def update_a_degree_route_staff():
    if request.method == "POST" and session.get("type") == "staff":
        put_a_degree_to_api(
            request.form.get("id"),
            request.form.get("degree_id"),
            request.form.get("name_degree"),
            request.form.get("description")
        )
        return redirect("/staff/pannel")
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

@app.route("/staff/pannel/updateproject",methods=["POST"])
def update_a_project_route_staff():
    if request.method == "POST" and session.get("type") == "staff":
        put_a_project_to_api(
            request.form.get("id"),
            request.form.get("project_id"),
            request.form.get("name_project"),
            request.form.get("description")
        )
        return redirect("/staff/pannel")
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
        return redirect("/")
    
    credentials = get_credentials_from_api()

    for obj in credentials:
        if obj["email"] == email and obj["type"] == "admin":
            if bcrypt.checkpw(password.encode('utf-8'), obj["hash"].encode('utf-8')):
                #CREATE SESSION!
                session["name"] = obj["email"]
                session["lang"] = obj["lang"]
                session["type"] = obj["type"]
                return redirect("/admin/list")
    return redirect("/")

@app.route("/staff/login", methods=["POST"])
def validate_staff_login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return redirect("/")
    
    credentials = get_credentials_from_api()

    for obj in credentials:
        if obj["email"] == email and obj["type"] == "staff":
            if bcrypt.checkpw(password.encode('utf-8'), obj["hash"].encode('utf-8')):
                #CREATE SESSION!
                session["name"] = obj["email"]
                session["lang"] = obj["lang"]
                session["type"] = obj["type"]
                return redirect("/staff/list")
    return redirect("/")


@app.route("/employer/login", methods=["POST"])
def validate_employer_login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    if not email or not password:
        return redirect("/")
    
    credentials = get_credentials_from_api()

    for obj in credentials:
        if obj["email"] == email:
            if bcrypt.checkpw(password.encode('utf-8'), obj["hash"].encode('utf-8')):
                #CREATE SESSION!
                session["name"] = obj["email"]
                session["lang"] = obj["lang"]

                if obj['type'] == "employer":
                    session["type"] = "employer"
                if obj['type'] == "staff":
                    session["type"] = "staff"
                if obj['type'] == "admin":
                    session["type"] = "admin"
                
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
    if request.method == "POST" and session.get("type") == "staff":
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
                return redirect("/staff/list")
        return redirect("/staff/list")
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
            request.form.get("pdf"),
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
            request.form.get("pdf"),
            status=request.form.get("status")
        )
        return redirect('/staff/list')
    return redirect("/")

@app.route("/admin/filter", methods=["POST"])
def adminFilterRoute():
    if session.get("type") == "admin":

        minimum = request.form.get("minimum")
        maximum = request.form.get("maximum")
        technologies = request.form.get("Technologies")
        degree = request.form.get("degree")
        professor_name = request.form.get("professor_name")
        project = request.form.get("project")

        filtered_students = get_all_students_from_api()

        if minimum != "":
            filtered_students = filter(lambda s: s["year_of_graduation"] >= minimum, filtered_students)
        if maximum  != "":
            filtered_students = filter(lambda s: s["year_of_graduation"] <= maximum, filtered_students)
        if professor_name  != "":
            filtered_students = filter(lambda s: professor_name.lower() in s["professor_name"].lower(), filtered_students)
        if technologies  != "":
            tech_list = technologies.lower().split()
            filtered_students = filter(lambda s: any(lang in s["programming_language"].lower().split() for lang in tech_list), filtered_students)
        if degree  != "":
            filtered_students = filter(lambda s: s["degree"] == degree, filtered_students)
        if project  != "":
            filtered_students = filter(lambda s: s["projectId"] == project, filtered_students)

        result = list(filtered_students)

        return render_template("list/filtered-admin-list.html", STUDENTS = result, I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"))
    
    return redirect("/")




@app.route("/staff/filter", methods=["POST"])
def staffFilterRoute():
    if session.get("type") == "staff":
        
        minimum = request.form.get("minimum")
        maximum = request.form.get("maximum")
        technologies = request.form.get("Technologies")
        degree = request.form.get("degree")
        professor_name = request.form.get("professor_name")
        project = request.form.get("project")

        filtered_students = get_all_students_from_api()

        if minimum != "":
            filtered_students = filter(lambda s: s["year_of_graduation"] >= minimum, filtered_students)
        if maximum  != "":
            filtered_students = filter(lambda s: s["year_of_graduation"] <= maximum, filtered_students)
        if professor_name  != "":
            filtered_students = filter(lambda s: professor_name.lower() in s["professor_name"].lower(), filtered_students)
        if technologies  != "":
            tech_list = technologies.lower().split()
            filtered_students = filter(lambda s: any(lang in s["programming_language"].lower().split() for lang in tech_list), filtered_students)
        if degree  != "":
            filtered_students = filter(lambda s: s["degree"] == degree, filtered_students)
        if project  != "":
            filtered_students = filter(lambda s: s["projectId"] == project, filtered_students)

        result = list(filtered_students)

        return render_template("list/filtered-staff-list.html", STUDENTS = result, I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"))
    
    return redirect("/")

@app.route("/employer/filter", methods=["POST"])
def employerFilterRoute():
    if session.get("type") == "employer":
        
        minimum = request.form.get("minimum")
        maximum = request.form.get("maximum")
        technologies = request.form.get("Technologies")
        degree = request.form.get("degree")
        professor_name = request.form.get("professor_name")
        project = request.form.get("project")

        filtered_students = get_all_students_from_api()

        if minimum != "":
            filtered_students = filter(lambda s: s["year_of_graduation"] >= minimum, filtered_students)
        if maximum  != "":
            filtered_students = filter(lambda s: s["year_of_graduation"] <= maximum, filtered_students)
        if professor_name  != "":
            filtered_students = filter(lambda s: professor_name.lower() in s["professor_name"].lower(), filtered_students)
        if technologies  != "":
            tech_list = technologies.lower().split()
            filtered_students = filter(lambda s: any(lang in s["programming_language"].lower().split() for lang in tech_list), filtered_students)
        if degree  != "":
            filtered_students = filter(lambda s: s["degree"] == degree, filtered_students)
        if project  != "":
            filtered_students = filter(lambda s: s["projectId"] == project, filtered_students)

        result = list(filtered_students)

        return render_template("list/filtered-employer-list.html", STUDENTS = result, I18N=i18n, LANG=session.get("lang"), EMAIL=session.get("name"))
    
    return redirect("/")

##
@app.route("/employer/email", methods=["POST"])
def email_students_route():
    if session.get("type") == "employer":

        list_of_students = []

        emails = request.form.getlist('student')

        if len(emails)==0:
            return render_template("email_sent.html", STUDENT_NAME="no student selected",EMAIL=session.get("name"),I18N=i18n,SENT=False,LANG=session.get("lang"),LENGTH=0) 

        for i in emails:
            student = get_one_student_from_api(i)
            list_of_students.append({"name":student["first_name"],"resume":student["resume"]})

        sent_bool = send_mail(session.get("name"),list_of_students)
        
        if len(emails) == 1:
            return render_template("email_sent.html", STUDENT_NAME=list_of_students[0]["name"],EMAIL=session.get("name"),I18N=i18n,SENT=sent_bool,LANG=session.get("lang"),LENGTH=1)
        if len(emails) > 1:
            return render_template("email_sent.html", STUDENT_NAME=list_of_students[0]["name"],EMAIL=session.get("name"),I18N=i18n,SENT=sent_bool,LANG=session.get("lang"),LENGTH=2)
    return redirect("/")
###


@app.route("/admin/list/resume",methods=["POST"])
def admin_view_resume_route():
    if session.get("type") == "admin":

        base64_string = request.form.get("pdf")
        pdf_data = base64.b64decode(base64_string)
        response = make_response(pdf_data)
        response.headers.set('Content-Disposition', 'inline', filename='file.pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response

    return redirect("/")

@app.route("/staff/list/resume",methods=["POST"])
def staff_view_resume_route():
    if session.get("type") == "staff":

        base64_string = request.form.get("pdf")
        pdf_data = base64.b64decode(base64_string)
        response = make_response(pdf_data)
        response.headers.set('Content-Disposition', 'inline', filename='file.pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response
    return redirect("/")

@app.route("/employer/list/resume",methods=["POST"])
def employer_view_resume_route():
    if session.get("type") == "employer":
        base64_string = request.form.get("pdf")
        pdf_data = base64.b64decode(base64_string)
        response = make_response(pdf_data)
        response.headers.set('Content-Disposition', 'inline', filename='file.pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response
    return redirect("/")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500

if __name__ == '__main__':
    app.run()