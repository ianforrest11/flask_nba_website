from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note')

class Player(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nba_player_id = db.Column(db.Integer)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    nba_team_id = db.Column(db.Integer)
    team_abbr = db.Column(db.String(30))
    age = db.Column(db.Integer)
    games_played = db.Column(db.Integer)
    games_started = db.Column(db.Integer)
    minutes = db.Column(db.Integer)
    fgm = db.Column(db.Integer)
    fga = db.Column(db.Integer)
    fg_pct = db.Column(db.Float)
    fg3m = db.Column(db.Integer)
    fg3a = db.Column(db.Integer)
    fg3_pct = db.Column(db.Float)
    ftm = db.Column(db.Integer)
    fta = db.Column(db.Integer)
    ft_pct = db.Column(db.Float)
    points = db.Column(db.Integer)
    orebounds = db.Column(db.Integer)
    drebounds = db.Column(db.Integer)
    rebounds = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    steals = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    turnovers = db.Column(db.Integer)
    fouls = db.Column(db.Integer)