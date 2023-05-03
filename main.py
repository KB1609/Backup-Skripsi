from flask import Flask, redirect, url_for, render_template, request
from .models import db, SearchHist, listuser
from .stockdata import stockdata
from . import app
from .auth import auth
from .Nav import Nav
import pandas as pd 
import secrets
    
@app.route("/")
def logout():

    return render_template("Login.html")
