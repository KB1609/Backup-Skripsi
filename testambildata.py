from flask import Flask, redirect,Blueprint, url_for, render_template, request
import yfinance as yf
import pandas as pd 
import os 

infos = yf.Ticker("MSFT")


# Get the company name
company_name = infos.info['longName']
print(company_name)