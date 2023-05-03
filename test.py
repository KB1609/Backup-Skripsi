import yfinance as yf

ticker = "AAPL"

myinfo = yf.Ticker(ticker).info

desc =  myinfo['longBusinessSummary']

desc