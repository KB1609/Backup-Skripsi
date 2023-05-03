from flask import Flask, redirect,Blueprint, url_for, render_template, request, session
from .util import listofuser, get_history_tables, get_watchlists_tables


Nav = Blueprint('Nav', __name__)

@Nav.route("/")
def homepages():
    session = request.environ.get('beaker.session')
    # Retrieve the UserId from the session
    # Get all history tables with matching UserId
    tables = get_history_tables()
    return render_template("index.html", tables=tables)


@Nav.route("/watchlistsstocks")
def watchlistsstocks():
    
    if session is not None and 'userid' in session and session['userid']:
        tables = get_watchlists_tables()
        data = tables[0]
        datatooltip = tables[1]
        return render_template("watchlist.html", tables=tables, datatooltip=datatooltip, data=data)
    else:
        return render_template("watchlist.html")
        # Handle case where userid is not set in session


@Nav.route("/watchlistspredict")
def watchlistspredict():
    session = request.environ.get('beaker.session')

    tables = get_watchlists_tables()
    data = tables[0]
    datatooltip = tables[1]
    return render_template("watchlistpredict.html", tables=tables, datatooltip = datatooltip, data = data)
