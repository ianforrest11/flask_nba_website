from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User_Player
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('note is too short', category='error')
        else:
            new_note = Note(data=note, user_id= current_user.id)
            db.session.add(new_note)
            db.session.commit()

            flash('note added', category='success')


    return render_template("home.html", user = current_user)

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/delete-player', methods = ['POST'])
def delete_player():
    user_player = json.loads(request.data)
    user_player_id = User_Player.query.get(user_player['user_player_id'])
    user_player = User_Player.query.get(user_player_id)
    if user_player:
        if user_player.user_player_id == current_user.id:
            db.session.delete(user_player)
            db.session.commit()
    return jsonify({})
