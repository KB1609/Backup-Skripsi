from flask import Flask, Blueprint, g
import sqlite3
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from flask_sqlalchemy import SQLAlchemy

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
    # UserId = db.Column(db.Integer)
    UserId = db.Column(db.Integer, ForeignKey('UserTable.UserId'))

class Prediction(db.Model):
    __tablename__ = 'Prediction'
    PredictionId = db.Column(db.Integer, primary_key=True)
    PedictionName = db.Column(db.Text)
    PedictionResult = db.Column(db.BLOB)
    ModelDataId = db.Column(db.Integer, ForeignKey('ModelData.ModelDataId'))
    model_data = relationship('ModelData', backref='predictions')

class ModelData(db.Model):
    __tablename__ = 'ModelData'
    ModelDataId = db.Column(db.Integer, primary_key=True)
    Symbol = db.Column(db.Text)
    NamaSaham = db.Column(db.Text)
    Data_Saham = db.Column(db.BLOB)
    Date = db.Column(db.Integer)

class WatchlistsPrediction(db.Model):
    __tablename__ = 'WatchlistsPrediction'
    WatchlistId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, ForeignKey('UserTable.UserId'))
    PredictionId = db.Column(db.Integer, ForeignKey('Prediction.PredictionId'))

# joinedprediction = db.session.query(Prediction, ModelData).join(ModelData).all()

# joinedWatchlistsPrediction = db.session.query(listuser, WatchlistsPrediction).join(WatchlistsPrediction).all()

