import os

from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from tempfile import mkdtemp
from flask_mysqldb import MySQL
from flask_session import Session
from app import *
from passlib.hash import bcrypt
from datetime import date
from . import main
from .forms import Model_1

main = Blueprint('main', __name__)

def execute_db(query,args=()):
    try:
        cur=mysql.connection.cursor()
        cur.execute(query,args)
        mysql.connection.commit()
    except:
        mysql.connection.rollback()
    finally:
        cur.close()

def preprocessing(file):

    # your preprocessing code here

    return file

def predict(file):

    # your model prediction output code here

    return file


@main.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@main.route("/aboutus/", methods=["POST", "GET"])
def about():
    return render_template("aboutus.html")

@main.route('/logout/', methods=["GET", "POST"])
@login_required
def logout():
    session.clear()
    return redirect(url_for("main.index"))

@main.route("/login/", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        username = request.form["id"]
        password = request.form["pass"]
        query  = query_db("SELECT password FROM t_nbsu WHERE n_id=%s;",(username, ))
        if query is None:
            flash("Incorrect Credentials!", "danger")
            return redirect(url_for('main.login'))
        else:
            if bcrypt.verify(password, query[0][0]):
                session["n_id"] = username
                flash("Login Successful", "success")
                return render_template("nbsu_portal.html", **locals())
    
            else:
                flash("Incorrect Credentials", "danger")
                return redirect(url_for('main.login_view'))
    return render_template("nbsu_login.html", **locals())
 
@main.route('/model1', methods=['GET', 'POST'])
@login_required
def model1():
    form = Model_1()
    if form.validate_on_submit():
        file = form.data.data
        filename = file.filename
        file_path = os.path.join('.', filename)
        file.save(file_path)
        return filename
    return render_template('Model_1.html', form = form)     

@main.route('/add/', methods=["GET", "POST"])
@teacher_required
def add():
    if request.method=="POST":
        print(request.form)
        
        execute_db("INSERT INTO student(mrn, adm_m, adm_y, outcome, dist) VALUES (%s, %s, %s, %s, %s);", (mrn, adm_m, adm_y, outcome, dist, ))
        flash("Data Inserted Successfully!","success")
        return redirect(url_for('main.add'))

    return render_template("add_info.html")

@main.route('/add/', methods=["GET", "POST"])
@teacher_required
def add():
    if request.method=="POST":
        print(request.form)
        
        execute_db("INSERT INTO student(mrn, adm_m, adm_y, outcome, dist) VALUES (%s, %s, %s, %s, %s);", (mrn, adm_m, adm_y, outcome, dist, ))
        flash("Data Inserted Successfully!","success")
        return redirect(url_for('main.add'))

    return render_template("add_info.html")
