from flask import Blueprint, render_template, request, flash, redirect, url_for
from markupsafe import re
from .models import Player, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import sqlite3

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category = 'success')
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category = 'error')
        else:
            flash('email does not exist', category= 'error')

    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('email already exists', category='error')

        elif len(email) < 4:
            flash("Email must be greater than three characters", category = 'error')
        elif len(firstName) < 2:
            flash("First name must be greater than one characters", category = 'error')
        elif password1 != password2:
            flash("Passwords are not equal", category = 'error')
        elif len(password1) < 7:
            flash("Password must be at least seven characters", category = 'error')
        else:
            # add user to database
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account Created", category = 'success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user = current_user)

@auth.route('/stats_pg', methods = ['GET'])
def stats_pg():

    user = User.query.filter_by(email='ian@gmail.com').first()
    
    conn = sqlite3.connect('test_database.db')
    c = conn.cursor()

    # per game stats
    c.execute("DROP TABLE IF EXISTS pg_stats")

    c.execute('''
    CREATE TABLE pg_stats
    AS
    SELECT first_name AS "First Name", last_name AS "Last Name", team_abbr as "Team", age AS "Age", games_played AS "GP", games_started AS "GS",
    ROUND(CAST(minutes AS float(1))/CAST(games_played AS float(1)), 1) AS "MPG",
    ROUND(CAST(fgm AS float(1))/CAST(games_played AS float(1)), 1) AS "FGMPG",
    ROUND(CAST(fga AS float(1))/CAST(games_played AS float(1)), 1) AS "FGAPG",
    fg_pct AS "FG%",
    ROUND(CAST(fg3m AS float(1))/CAST(games_played AS float(1)), 1) AS "3MPG",
    ROUND(CAST(fg3a AS float(1))/CAST(games_played AS float(1)), 1) AS "3APG",
    fg3_pct AS "3FG%",
    ROUND(CAST(ftm AS float(1))/CAST(games_played AS float(1)), 1) AS "FTMPG", 
    ROUND(CAST(fta AS float(1))/CAST(games_played AS float(1)), 1) AS "FTAPG",
    ft_pct AS "FT%",
    ROUND(CAST(points AS float(1))/CAST(games_played AS float(1)), 1) AS "PPG",
    ROUND(CAST(orebounds AS float(1))/CAST(games_played AS float(1)), 1) AS "ORPG",
    ROUND(CAST(drebounds AS float(1))/CAST(games_played AS float(1)), 1) AS "DRPG",
    ROUND(CAST(rebounds AS float(1))/CAST(games_played AS float(1)), 1) AS "RPG",
    ROUND(CAST(assists AS float(1))/CAST(games_played AS float(1)), 1) AS "APG",
    ROUND(CAST(steals AS float(1))/CAST(games_played AS float(1)), 1) AS "SPG",
    ROUND(CAST(blocks AS float(1))/CAST(games_played AS float(1)), 1) AS "BPG", 
    ROUND(CAST(turnovers AS float(1))/CAST(games_played AS float(1)), 1) AS "TPG",
    ROUND(CAST(fouls AS float(1))/CAST(games_played AS float(1)), 1) AS "FPG" 
    FROM player_stats_2122;''')
    players_query = c.execute('''SELECT * FROM pg_stats''').fetchall()

    columns = c.execute("PRAGMA table_info(pg_stats)")
    columns_query = [item[1] for item in columns.fetchall()]

    # Totals
    c.execute("DROP TABLE IF EXISTS display_stats")

    c.execute('''
    CREATE TABLE display_stats
    AS
    SELECT first_name AS "First Name", last_name AS "Last Name", team_abbr as "Team",
    age AS "Age", games_played AS "GP", games_started AS "GS", minutes AS "MIN", fgm AS "FGM", fga AS "FGA",
    fg_pct AS "FG%", fg3m AS "3FGM", fg3a AS "3FGA", fg3_pct AS "3FG%", ftm AS "FTM", fta AS "FTA", ft_pct AS "FT%", points AS "PTS",
    orebounds AS "OREB", drebounds AS "DREB", rebounds AS "REB", assists AS "AST", steals AS "STL", blocks AS "BLK", 
    turnovers AS "TOV", fouls AS "PF" 
    FROM player_stats_2122;''')
    players_query_totals = c.execute('''SELECT * FROM display_stats''').fetchall()

    columns_totals = c.execute("PRAGMA table_info(display_stats)")
    columns_query_total = [item[1] for item in columns.fetchall()]

    conn.close()


    return render_template('stats_pg.html', feed=players_query, user = user, columns = columns_query,
                            feed2 = players_query_totals, columns2 = columns_query_total)

@auth.route('/stats', methods = ['GET'])
def stats():

    user = User.query.filter_by(email='ian@gmail.com').first()
    
    conn = sqlite3.connect('test_database.db')
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS display_stats")

    c.execute('''
    CREATE TABLE display_stats
    AS
    SELECT first_name AS "First Name", last_name AS "Last Name", team_abbr as "Team",
    age AS "Age", games_played AS "GP", games_started AS "GS", minutes AS "MIN", fgm AS "FGM", fga AS "FGA",
    fg_pct AS "FG%", fg3m AS "3FGM", fg3a AS "3FGA", fg3_pct AS "3FG%", ftm AS "FTM", fta AS "FTA", ft_pct AS "FT%", points AS "PTS",
    orebounds AS "OREB", drebounds AS "DREB", rebounds AS "REB", assists AS "AST", steals AS "STL", blocks AS "BLK", 
    turnovers AS "TOV", fouls AS "PF" 
    FROM player_stats_2122;''')
    players_query = c.execute('''SELECT * FROM display_stats''').fetchall()

    columns = c.execute("PRAGMA table_info(display_stats)")
    columns_query = [item[1] for item in columns.fetchall()]

    conn.close()


    return render_template('stats.html', feed=players_query, user = user, columns = columns_query)

@auth.route('/test', methods = ['GET'])
def test():
    return render_template('test.html')