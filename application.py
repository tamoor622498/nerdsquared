import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("DATABASE URL")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    allSites = db.execute("SELECT * FROM sites").fetchall()
    buttonNames = set()
    for site in allSites:
        buttonNames.add((site.tag).capitalize())
    buttonNames = list(buttonNames)
    buttonNames.sort()
    curr = "All sites"
    db.commit()
    return render_template("menuAndSites.html", curr=curr, buttonNames=buttonNames, allSites=allSites)

@app.route("/<string:name>")
def tags(name):
    allSites = db.execute("SELECT * FROM sites").fetchall()
    buttonNames = set()
    for site in allSites:
        buttonNames.add((site.tag).capitalize())
    buttonNames = list(buttonNames)
    buttonNames.sort()
    curr = name
    allSites = db.execute("SELECT * FROM sites WHERE tag=\'"+name.lower()+"\'").fetchall()
    db.commit()
    return render_template("menuAndSites.html", curr=curr, buttonNames=buttonNames, allSites=allSites)
