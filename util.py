from .models import db, SearchHist, listuser
from flask import session
from . import app

import yfinance as yf

with app.app_context():
    def savehistory(keyword, UserId):
        
        # check if the keyword with the given UserId already exists
        existing_keyword = SearchHist.query.filter_by(SymbolKeyword=keyword, UserId=UserId).first()
        if existing_keyword:
            return False
        
        # create a new row in the SearchHistory table with the given text and UserId
        new_search_history = SearchHist(SymbolKeyword=keyword, UserId=UserId)
        db.session.add(new_search_history)
        db.session.commit()
        return True
    

def get_history_tables():
    with app.app_context():
        # Retrieve the UserId from the session
        UserId = session.get('userid')
        # Query the SearchHist table to get all rows with matching UserId
        historytable = SearchHist.query.filter_by(UserId=UserId).all()
        # Return the resulting rows
        return historytable
    

def get_watchlists_tables():
    with app.app_context():
       # Retrieve the UserId from the session
        UserId = session.get('userid')
        # Query the SearchHist table to get all rows with matching UserId

        if UserId is not None:

            
            historytable = SearchHist.query.filter_by(UserId=UserId).all()

            # Create a list to store the data
            watchlist_data = []
            watchlist_datatooltip = []

            # Iterate over the historytable and extract the relevant data
            for row in historytable:
                
                
                data = {
                    'nama': 'yakin',
                    'symbols': row.SymbolKeyword

                }

                datatooltip = {
                    'nama': 'halo'

                }
                # Download custom data using yfinance
                symbol = row.SymbolKeyword
                
                # custom_data = yf.download(symbol, period = "1y")
                datas= yf.download(f"{symbol}", period="1y")

                info = yf.Ticker(symbol)
                longname = info.info['longName']
                currency = info.info['currency']

                labels = datas.index.strftime('%Y-%m-%d').tolist()
                values = datas['Adj Close'].tolist()
                
                #add customdata to dictionary
                data['longname'] = longname
                data['currency'] = currency
                data['labels'] = labels
                data['values'] = values

                Open = datas["Open"].tolist()
                High = datas["High"].tolist()
                Low = datas["Low"].tolist()
                Close = datas["Close"].tolist()
                Volume = datas["Volume"].tolist()

                #add customdata tooltips to dictionary
                datatooltip['open_data'] = Open
                datatooltip['high_data'] = High
                datatooltip['low_data'] = Low
                datatooltip['close_data'] = Close
                datatooltip['volume_data'] = Volume

                
                # # Add custom data to the data dictionary
                # data['custom_data'] = custom_data.to_dict()
                # data['custom_data'] = custom_data.to_dict()
                # Append the extracted data to the list

                #append datadictionary to lists
                watchlist_data.append(data)
                watchlist_datatooltip.append(datatooltip)

                my_data = watchlist_data
                my_datatooltip = watchlist_datatooltip

            # Return the list of extracted data
            return (my_data, my_datatooltip, my_data)
        else :
            my_data = []
            return my_data
    
    
class listofuser():
    @staticmethod
    def get_user_tables():
        usertables = listuser.query.all()
        return usertables

