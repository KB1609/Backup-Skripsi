from flask import Flask, flash, redirect,Blueprint, url_for, render_template, request, g, session
import os 
from .models import listuser

# from Conn import get_db
auth = Blueprint('auth', __name__)


@auth.route("/LoginPage")
def loginpage():

    return render_template("Login.html")

@auth.route("/logout")
def logout():

    session.pop('username', None)
    session.pop('userid', None)
    return render_template("Login.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = listuser.query.filter_by(UserName=username, Password=password).first()
        if user:
            session['username'] = user.UserName
            session['userid'] = user.UserId
            return redirect(url_for('Nav.homepages'))
        else:
            flash('*Invalid username or password', 'error')
        return render_template('Login.html')
    else:
        return render_template('Login.html')
