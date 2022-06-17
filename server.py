import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for

POINTS_FOR_A_PLACE = 3
MAX_PLACES_PER_COMPETITION = 12


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def write_to_json(file_name, my_dict, var_name):
    with open(file_name, 'w') as file:
        json.dump({var_name: my_dict}, file, indent=4)



app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        flash("Sorry, that email wasn't found.")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition,club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
    except IndexError:
        foundClub = None
        foundCompetition = None
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if foundClub and foundCompetition:
        if foundCompetition['date'] < date_time:
            flash("You cannot book places in past competition")
            return render_template("welcome.html", club=foundClub, competitions=competitions)
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=foundClub, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    places_allowed = int(club["points"]) // POINTS_FOR_A_PLACE
    if placesRequired > places_allowed:
        flash('You cannot redeem more points than available!')
    elif placesRequired > MAX_PLACES_PER_COMPETITION:
        flash(f"You cannot book more than {MAX_PLACES_PER_COMPETITION} places per competition!")
    elif placesRequired > int(competition['numberOfPlaces']):
        flash(f"You cannot reserve more places than are available in the competition!")
    else:
        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces']) - placesRequired)
        club["points"] = str(places_allowed - placesRequired * POINTS_FOR_A_PLACE)
        write_to_json('clubs.json', clubs,'clubs')
        write_to_json('competitions.json', competitions, 'competitions')
        flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/displayPointsBoard')
def display_points_board():
    return render_template('points_board.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))