from flask import Flask, render_template, request, redirect, url_for
from flask import session
import pymysql
import time
import os

from werkzeug.utils import secure_filename

from mylib import make_connection, check_photo

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = './static/photos'


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        med_name = request.form["T1"]
        cur = make_connection()
        sql = "select * from medicine_medical where med_name like '%" + med_name + "%'"
        cur.execute(sql)
        n = cur.rowcount
        if n > 0:
            records = cur.fetchall()
            return render_template("Home.html", data=records)
        else:
            return render_template("Home.html", msg="No records found")
    else:
        return render_template("Home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["T1"]
        password = request.form["T2"]
        cur = make_connection()
        sql = "select * from login_data where email='" + email + "' and password='" + password + "'"
        cur.execute(sql)
        n = cur.rowcount
        if n == 1:
            data = cur.fetchone()
            # fetch usertype from index 2
            ut = data[2]
            # creating sessions
            session["ut"] = ut
            session["email"] = email

            if ut == "admin":
                return redirect(url_for("admin_home"))
            elif ut == "medical":
                return redirect(url_for("medical_home"))
            else:
                return render_template("login.html", msg="contact to admin")
        else:
            return render_template("login.html", msg="Either email or password is incorrect")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    if "email" in session:
        session.pop("email", None)
        session.pop("ut", None)
        return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))


@app.route("/adminreg", methods=["GET", "POST"])
def adminreg():
    if "email" in session:
        ut = session["ut"]
        if ut == "admin":
            if request.method == "POST":
                name1 = request.form["T1"]
                name2 = request.form["T11"]
                address = request.form["T2"]
                a1 = request.form["T21"]
                a2 = request.form["T22"]
                a3 = request.form["T23"]
                contact = request.form["T3"]
                email = request.form["T4"]
                password = request.form["T5"]
                usertype = "admin"
                cur = make_connection()
                sql1 = "insert into admin_data values('" + name1 + " " + name2 + "','" + address + " " + a1 + " " + a2 + " " + a3 + "','" + contact + "','" + email + "')"
                sql2 = "insert into login_data values('" + email + "','" + password + "','" + usertype + "')"
                msg = ""
                try:
                    cur.execute(sql1)
                    n1 = cur.rowcount
                    cur.execute(sql2)
                    n2 = cur.rowcount

                    if n1 == 1 and n2 == 1:
                        msg = "Data Saved and Login Created sucessfully"
                    elif n1 == 1:
                        msg = "Data Saved succesfully"
                    elif n2 == 1:
                        msg = "Login Created successfully"
                    else:
                        msg = "Error found "
                except pymysql.err.IntegrityError:
                    msg="This email is already registered"
                return render_template("AdminReg.html", kota=msg)
            else:
                return render_template("AdminReg.html")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/admin_pass_change", methods=["GET", "POST"])
def admin_pass_change():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "admin":
            if request.method == "POST":
                a = request.form["t1"]
                b = request.form["t2"]
                cn = pymysql.connect(host="localhost", user="root", port=3306, passwd="", db="govind", autocommit=True)
                cur = cn.cursor()
                sql = "update login_data set password='" + b + "' where email='" + email + "' and password='" + a + "'"
                cur.execute(sql)
                n = cur.rowcount
                if n == 1:
                    return render_template("AdminChangePassword.html", msg="Password Changed")
                else:
                    return render_template("AdminChangePassword.html", msg="Invalid Old Password")
            else:
                return render_template("AdminChangePassword.html")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/medical_pass_change", methods=["GET", "POST"])
def medical_pass_change():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "medical":
            if request.method == "POST":
                a = request.form["t1"]
                b = request.form["t2"]
                cn = pymysql.connect(host="localhost", user="root", port=3306, passwd="", db="govind", autocommit=True)
                cur = cn.cursor()
                sql = "update login_data set password='" + b + "' where email='" + email + "' and password='" + a + "'"
                cur.execute(sql)
                n = cur.rowcount
                if n == 1:
                    return render_template("MedicalChangePassword.html", msg="Password Changed")
                else:
                    return render_template("MedicalChangePassword.html", msg="Invalid Old Password")
            else:
                return render_template("MedicalChangePassword.html")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/show_admin")
def show_admin():
    cur = make_connection()
    sql = "select * from admin_data"
    cur.execute(sql)
    n = cur.rowcount
    if n > 0:
        records = cur.fetchall()
        return render_template("ShowAdminRecords.html", data=records)
    else:
        return render_template("ShowAdminRecords.html", msg="Data not Found")


@app.route("/medicalreg", methods=["GET", "POST"])
def medicalreg():
    if "email" in session:
        ut = session["ut"]
        if ut == "admin":
            if request.method == "POST":
                a = request.form["t1"]
                b = request.form["t2"]
                b2 = request.form["t21"]
                c = request.form["t3"]
                d = request.form["t4"]
                d1 = request.form["t41"]
                d2 = request.form["t42"]
                d3 = request.form["t43"]
                e = request.form["t5"]
                f = request.form["t6"]
                g = request.form["t7"]
                ut = "medical"
                cur = make_connection()
                s1 = "insert into medical_data (mname,owner,lno,address,contact,email) values('" + a + "','" + b + " " + b2 + "','" + c + "','" + d + " " + d1 + " " + d2 + " " + d3 + "','" + e + "','" + f + "')"
                s2 = "insert into login_data values('" + f + "','" + g + "','" + ut + "')"
                msg=""
                try:
                    cur.execute(s1)
                    n1 = cur.rowcount
                    cur.execute(s2)
                    n2 = cur.rowcount
                    if n1 == 1 and n2 == 1:
                        msg = "Data Saved and Login Created sucessfully"
                    elif n1 == 1:
                        msg = "Data Saved succesfully"
                    elif n2 == 1:
                        msg = "Login Created successfully"
                    else:
                        msg = "Error Occured"
                except pymysql.err.IntegrityError:
                    msg="This email is already registered"
                return render_template("MedicalReg.html", res=msg)
            else:
                return render_template("MedicalReg.html")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/show_medicals")
def show_medicals():
    if "email" in session:
        ut = session["ut"]
        if ut == "admin":
            cur = make_connection()
            sql = "select * from medical_data"
            cur.execute(sql)
            n = cur.rowcount
            if n > 0:
                records = cur.fetchall()
                return render_template("AllMedicals.html", data=records)
            else:
                return render_template("AllMedicals.html", msg="No records found")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/show_medicals_home")
def show_medicals_home():
    cur = make_connection()
    sql = "select * from medical_data"
    cur.execute(sql)
    n = cur.rowcount
    if n > 0:
        records = cur.fetchall()
        return render_template("ShowMedicals.html", data=records)
    else:
        return render_template("ShowMedicals.html", msg="No Data Found")


@app.route("/admin_home")
def admin_home():
    if "email" in session:
        email = session["email"]  # email of logged-in user
        ut = session["ut"]
        if ut == "admin":
            photo = check_photo(email)
            cur = make_connection()
            sql = "select * from admin_data where email='" + email + "'"
            cur.execute(sql)
            n = cur.rowcount
            if n == 1:
                record = cur.fetchone()
                return render_template("AdminHome.html", data=record, e1=email, photo=photo)
            else:
                return render_template("AdminHome.html", msg="No Profile Found")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


# for uloading photo
@app.route("/admin_photo")
def admin_photo():
    return render_template("AdminPhotoUpload.html")


@app.route("/admin_photo_1", methods=["GET", "POST"])
def admin_photo_1():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "admin":
            if request.method == "POST":
                file = request.files["F1"]
                if file:
                    path = os.path.basename(file.filename)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) + '.' + file_ext
                    filename = secure_filename(filename)
                    cur = make_connection()
                    sql = "insert into photo_data values('" + email + "','" + filename + "')"

                    try:
                        cur.execute(sql)
                        n = cur.rowcount
                        if n == 1:
                            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                            return render_template('AdminPhotoUpload1.html', result="success")
                        else:
                            return render_template('AdminPhotoUpload1.html', result="failure")
                    except:
                        return render_template('AdminPhotoUpload1.html', result="duplicate")
                else:
                    return render_template('AdminPhotoUpload.html')
            else:
                return redirect(url_for('autherror'))
        else:
            return redirect(url_for('autherror'))
    else:
        return redirect(url_for("autherror"))


@app.route("/change_admin_photo")
def change_admin_photo():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "admin":
            photo = check_photo(email)
            cur = make_connection()
            sql = "delete from photo_data where email='" + email + "'"
            cur.execute(sql)
            n = cur.rowcount
            if n > 0:
                os.remove("./static/photos/" + photo)
                return render_template("ChangeAdminPhoto.html", msg="Success")
            else:
                return render_template("ChangeAdminPhoto.html", msg="Error!! Photo Not Changed")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/medical_home")
def medical_home():
    if "email" in session:
        email = session["email"]
        ut = session["ut"]
        if ut == "medical":
            cur = make_connection()
            sql = "select * from medical_data where email='" + email + "'"
            cur.execute(sql)
            n = cur.rowcount
            if n == 1:
                record = cur.fetchone()
                return render_template("MedicalHome.html", data=record)
            else:
                return render_template("MedicalHome.html", msg="No Data Found")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/medical_photo")
def medical_photo():
    return render_template("MedicalPhotoUpload.html")


@app.route("/medical_photo_1", methods=["GET", "POST"])
def medical_photo_1():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "admin" or ut == "medical":
            if request.method == "POST":
                file = request.files["F1"]
                if file:
                    path = os.path.basename(file.filename)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) + '.' + file_ext
                    filename = secure_filename(filename)
                    cur = make_connection()
                    sql = "update medical_data set photo_medical='" + filename + "'where email='" + email + "'"

                    try:
                        cur.execute(sql)
                        n = cur.rowcount
                        if n == 1:
                            file.save(os.path.join('./static/medicalphotos', filename))
                            return render_template("MedicalPhotoUpload1.html", result="success")
                        else:
                            return render_template("MedicalPhotoUpload1.html", result="failure")
                    except:
                        return render_template("MedicalPhotoUpload1.html", result="Photo Already Uploaded")
                else:
                    return render_template("MedicalPhotoUpload.html")
            else:
                return redirect(url_for("autherror"))
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/change_medical_photo", methods=["GET", "POST"])
def change_medical_photo():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "admin" or ut == "medical":
            if request.method == "POST":
                email = request.form["H1"]
                photo = request.form["H2"]
                cur = make_connection()
                sql = "update medical_data set photo_medical='no' where email='" + email + "'"
                cur.execute(sql)
                n = cur.rowcount
                if n == 1:
                    os.remove("./static/medicalphotos/" + photo)
                    return render_template("ChangeMedicalPhoto.html", msg="Photo Deleted")
                else:
                    return render_template("ChangeMedicalPhoto.html", msg="Photo Not Deleted")
            else:
                return render_template("MedicalHome.html")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/edit_admin_profile", methods=["GET", "POST"])
def edit_admin_profile():
    # chcking existanse of session
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "admin":
            cur = make_connection()
            sql = "select * from admin_data where email='" + email + "'"
            cur.execute(sql)
            n = cur.rowcount
            if n == 1:
                record = cur.fetchone()
                return render_template("AdminProfile.html", data=record)
            else:
                return render_template("AdminProfile.html", msg="No Data Found")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/edit_admin_profile_1", methods=["GET", "POST"])
def edit_admin_profile_1():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "admin":
            if request.method == "POST":
                a = request.form["t1"]
                b = request.form["t2"]
                c = request.form["t3"]
                cur = make_connection()
                sql = "update admin_data set namee='" + a + "',address='" + b + "',contact='" + c + "' where email='" + email + "'"
                cur.execute(sql)
                n = cur.rowcount
                if n == 1:
                    return render_template("AdminProfile1.html", msg="Data Saved Successfully")
                else:
                    return render_template("AdminProfile1.html", msg="Data Not Saved")
            else:
                return redirect(url_for("admin_home"))
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/med_upload", methods=["GET", "POST"])
def med_upload():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "medical":
            if request.method == "POST":
                a = request.form["t1"]
                b = request.form["t2"]
                c = request.form["t3"]
                d = request.form["t4"]
                e = request.form["t5"]
                cur = make_connection()
                med_id = 0
                sql = "insert into medicine_data values('" + str(
                    med_id) + "','" + a + "','" + b + "','" + c + "','" + str(d) + "','" + e + "','" + email + "')"
                cur.execute(sql)
                n = cur.rowcount
                if n == 1:
                    return render_template("MedUpload.html", msg="Medicine Uploaded")
                else:
                    return render_template("MedUpload.html", msg="Medicine Not Uploaded")
            else:
                return render_template("MedUpload.html")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/med_show", methods=["GET", "POST"])
def med_show():
    if "email" in session:
        ut = session["ut"]
        email = session["email"]
        if ut == "medical":
            cur = make_connection()
            sql = "select * from medicine_data where email_medical='" + email + "'"
            cur.execute(sql)
            n = cur.rowcount
            if n > 0:
                records = cur.fetchall()
                return render_template("MedShow.html", data=records)
            else:
                return render_template("MedShow.html", msg="No Data Found")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/delete_med", methods=["GET", "POST"])
def delete_med():
    if "email" in session:
        ut = session["ut"]
        if ut == "medical":
            med_id = request.form["t1"]
            cur = make_connection()
            sql = "delete from medicine_data where med_id='" + med_id + "'"
            cur.execute(sql)
            n = cur.rowcount
            if n == 1:
                return render_template("DeleteMed.html", msg="Data Deleted")
            else:
                return render_template("DeleteMed.html", msg="Data not Deleted")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/edit_med", methods=["GET", "POST"])
def edit_med():
    if "email" in session:
        ut = session["ut"]
        if ut == "medical":
            if request.method == "POST":
                med_id = request.form["t1"]
                cur = make_connection()
                sql = "select * from medicine_data where med_id='" + med_id + "'"
                cur.execute(sql)
                n = cur.rowcount
                if n == 1:
                    record = cur.fetchone()
                    return render_template("EditMed.html", data=record)
                else:
                    return render_template("EditMed.html", msg="Data not Found")
            else:
                return render_template("EditMed.html")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/edit_med_1", methods=["GET", "POST"])
def edit_med_1():
    if "email" in session:
        ut = session["ut"]
        if ut == "medical":
            medid = request.form["t1"]
            a = request.form["t2"]
            b = request.form["t3"]
            c = request.form["t4"]
            d = request.form["t5"]
            e = request.form["t6"]
            cur = make_connection()
            sql = "update medicine_data set med_name='" + a + "', company='" + b + "', l_no='" + c + "', price='" + d + "', remark='" + e + "' where med_id='" + medid + "'"
            cur.execute(sql)
            n = cur.rowcount
            if n == 1:
                return render_template("EditMed1.html", msg="Edited Successfully")
            else:
                return render_template("EditMed1.html", msg="Not Edited Successfully")
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/autherror")
def autherror():
    return render_template("AuthError.html")


@app.route("/edit_medical", methods=["GET", "POST"])
def edit_medical():
    if "email" in session:
        ut = session["ut"]
        if ut == "admin" or ut == "medical":
            if request.method == "POST":
                email = request.form["H1"]
                cur = make_connection()
                sql = "select * from medical_data where email='" + email + "'"
                cur.execute(sql)
                n = cur.rowcount
                if n == 1:
                    records = cur.fetchone()
                    return render_template("EditMedical.html", data=records)
                else:
                    return render_template("EditMedical.html", msg="No data Found")
            else:
                return redirect(url_for("show_medicals"))
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/edit_medical_1", methods=["GET", "POST"])
def edit_medical_1():
    if "email" in session:
        ut = session["ut"]
        if ut == "admin" or ut == "medical":
            if request.method == "POST":
                a = request.form["t1"]
                b = request.form["t2"]
                c = request.form["t3"]
                d = request.form["t4"]
                e = request.form["t5"]
                f = request.form["t6"]
                cur = make_connection()
                s1 = "update medical_data set mname='" + a + "',owner='" + b + "', lno='" + c + "',address='" + d + "',contact='" + e + "' where email='" + f + "'"
                cur.execute(s1)
                n = cur.rowcount
                if n == 1:
                    return render_template("EditMedical1.html", msg="Data Saved")
                else:
                    return render_template("EditMedical1.html", msg="Data Not Saved")
            else:
                return redirect(url_for("show_medicals"))
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/delete_medical", methods=["GET", "POST"])
def delete_medical():
    if "email" in session:
        ut = session["ut"]
        if ut == "admin" or ut == "medical":
            if request.method == "POST":
                email = request.form["H1"]
                cur = make_connection()
                sql = "select * from medical_data where email='" + email + "'"
                cur.execute(sql)
                n = cur.rowcount
                if n == 1:
                    records = cur.fetchone()
                    return render_template("DeleteMedical.html", data=records)
                else:
                    return render_template("DeleteMedical.html", msg="No data Found")
            else:
                return redirect(url_for("show_medicals"))
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


@app.route("/delete_medical_1", methods=["GET", "POST"])
def delete_medical_1():
    if "email" in session:
        ut = session["ut"]
        if ut == "admin" or ut == "medical":
            if request.method == "POST":
                f = request.form["t6"]
                cur = make_connection()
                s1 = "delete from medical_data where email='" + f + "'"
                s2 = "delete from login_data where email='" + f + "'"
                s2 = "delete from medicine_data where email='" + f + "'"
                cur.execute(s1)
                n = cur.rowcount
                cur.execute(s2)
                if n == 1:
                    return render_template("DeleteMedical1.html", msg="Data Deleted")
                else:
                    return render_template("DeleteMedical1.html", msg="Data Not Deleted")
            else:
                return redirect(url_for("show_medicals"))
        else:
            return redirect(url_for("autherror"))
    else:
        return redirect(url_for("autherror"))


# @app.route("/edit_medical_a", methods=["GET", "POST"])
# def edit_medical_a():
#     if "email" in session:
#         ut = session["ut"]
#         if ut == "medical":
#             if request.method == "POST":
#                 email = request.form["H1"]
#                 cur = make_connection()
#                 sql = "select * from medical_data where email='" + email + "'"
#                 cur.execute(sql)
#                 n = cur.rowcount
#                 if n == 1:
#                     records = cur.fetchone()
#                     return render_template("EditMedicalA.html", data=records)
#                 else:
#                     return render_template("EditMedicalA.html", msg="No data Found")
#             else:
#                 return redirect(url_for("medical_home"))
#         else:
#             return redirect(url_for("autherror"))
#     else:
#         return redirect(url_for("autherror"))
#
#
# @app.route("/edit_medical_a_1", methods=["GET", "POST"])
# def edit_medical_a_1():
#     if "email" in session:
#         ut = session["ut"]
#         if ut == "medical":
#             if request.method == "POST":
#                 a = request.form["t1"]
#                 b = request.form["t2"]
#                 c = request.form["t3"]
#                 d = request.form["t4"]
#                 e = request.form["t5"]
#                 f = request.form["t6"]
#                 cur = make_connection()
#                 s1 = "update medical_data set mname='" + a + "',owner='" + b + "', lno='" + c + "',address='" + d + "',contact='" + e + "' where email='" + f + "'"
#                 cur.execute(s1)
#                 n = cur.rowcount
#                 if n == 1:
#                     return render_template("EditMedicalA1.html", msg="Data Saved")
#                 else:
#                     return render_template("EditMedicalA1.html", msg="Data Not Saved")
#             else:
#                 return redirect(url_for("medical_home"))
#         else:
#             return redirect(url_for("autherror"))
#     else:
#         return redirect(url_for("autherror"))
#
#
# @app.route("/delete_medical_a", methods=["GET", "POST"])
# def delete_medical_a():
#     if "email" in session:
#         ut = session["ut"]
#         if ut == "medical":
#             if request.method == "POST":
#                 email = request.form["H1"]
#                 cur = make_connection()
#                 sql = "select * from medical_data where email='" + email + "'"
#                 cur.execute(sql)
#                 n = cur.rowcount
#                 if n == 1:
#                     records = cur.fetchone()
#                     return render_template("DeleteMedicalA.html", data=records)
#                 else:
#                     return render_template("DeleteMedicalA.html", msg="No data Found")
#             else:
#                 return redirect(url_for("medical_home"))
#         else:
#             return redirect(url_for("autherror"))
#     else:
#         return redirect(url_for("autherror"))
#
#
# @app.route("/delete_medical_a_1", methods=["GET", "POST"])
# def delete_medical_a_1():
#     if "email" in session:
#         ut = session["ut"]
#         if ut == "medical":
#             if request.method == "POST":
#                 f = request.form["t6"]
#                 cur = make_connection()
#                 s1 = "delete from medical_data where email='" + f + "'"
#                 s2 = "delete from login_data where email='" + f + "'"
#                 cur.execute(s1)
#                 n = cur.rowcount
#                 cur.execute(s2)
#                 if n == 1:
#                     return render_template("DeleteMedicalA1.html", msg="Data Deleted")
#                 else:
#                     return render_template("DeleteMedicalA1.html", msg="Data Not Deleted")
#             else:
#                 return redirect(url_for("medical_home"))
#         else:
#             return redirect(url_for("autherror"))
#     else:
#         return redirect(url_for("autherror"))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
