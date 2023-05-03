from flask import Flask, Blueprint, g
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Join

db = SQLAlchemy()


class listuser(db.Model):
    __tablename__ = 'UserTable'
    UserId = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.Text)
    Password = db.Column(db.Text)

class SearchHist(db.Model):
    __tablename__ = 'SearchHistory'
    HistoryId = db.Column(db.Integer, primary_key=True)
    SymbolKeyword = db.Column(db.Text)
    UserId = db.Column(db.Integer)
