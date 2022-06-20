import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for

POINTS_FOR_A_PLACE = 3
MAX_PLACES_PER_COMPETITION = 12


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


def write_to_json(file_name, my_dict, var_name):
    with open(file_name, 'w') as file:
        json.dump({var_name: my_dict}, file, indent=4)


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        flash("Sorry, that email wasn't found.")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    try:
        found_club = [c for c in clubs if c['name'] == club][0]
        found_competition = [c for c in competitions if c['name'] == competition][0]
    except IndexError:
        found_club = None
        found_competition = None
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if found_club and found_competition:
        if found_competition['date'] < date_time:
            flash("You cannot book places in past competition")
            return render_template("welcome.html", club=found_club, competitions=competitions)
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=found_club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    places_allowed = int(club["points"]) // POINTS_FOR_A_PLACE
    if places_required > places_allowed:
        flash('You cannot redeem more points than available!')
    elif places_required > MAX_PLACES_PER_COMPETITION:
        flash(f"You cannot book more than {MAX_PLACES_PER_COMPETITION} places per competition!")
    elif places_required > int(competition['numberOfPlaces']):
        flash(f"You cannot reserve more places than are available in the competition!")
    else:
        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces']) - places_required)
        club["points"] = str(int(club["points"]) - (places_required * POINTS_FOR_A_PLACE))
        write_to_json('clubs.json', clubs, 'clubs')
        write_to_json('competitions.json', competitions, 'competitions')
        flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/displayPointsBoard')
def display_points_board():
    return render_template('points_board.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
