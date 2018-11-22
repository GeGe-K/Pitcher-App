from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Pitch, Comment
import markdown2
from .forms import CommentForm, UpdateProfile, AddPitchForm
from .. import db,photos
from datetime import datetime
from flask_login import login_required,current_user


@main.route('/')
def index():

    pitches = Pitch.query.all()
    title = "Home"   
    return render_template("index.html", pitches = pitches, title = title)

@main.route('/pitches/<category>')
def categories(category):

    pitches = None
    if category == 'all':
        pitches = Pitch.query.order_by(Pitch.time.desc())
    else:
        pitches = Pitch.query.filter_by(category = category).order_by(Pitch.posted.desc())

    return render_template("pitch.html", pitches = pitches, title = category.upper())

@main.route("/<uname>/add_pitch", methods = ["GET","POST"])
@login_required
def add_pitch(uname):
    
    form = AddPitchForm()
    user = User.query.filter_by(username = uname).first()
  
    title = "Add Pitch"
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data 
        posted = datetime.now()
        new_pitch = Pitch(title = title, content = pitch, category = category,user = user, posted = posted)
        new_pitch.save_pitch()  
        pitches = Pitch.query.all()
        return redirect(url_for("main.categories",category = category))
    return render_template("add_pitch.html",form = form, title = title)

@main.route("/<user>/pitch/<pitch_id>/add-comment", methods = ["GET","POST"])
@login_required
def comment(user,pitch_id):
    user = User.query.filter_by(id = user).first()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    form = CommentForm()
    title = "Add comment"
    if form.validate_on_submit():
        content = form.comment.data 
        posted = datetime.now()
        new_comment = Comment(comment = form.comment.data, user = user, pitch = pitch, posted = posted )
        new_comment.save_comment()
        return redirect(url_for("main.view_comments", pitch_id=pitch.id))
    return render_template("new_comment.html", title = pitch.title,form = form,pitch = pitch)

@main.route("/<pitch_id>/comments")
@login_required
def view_comments(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    title = "Comments"
    comments = pitch.get_pitch_comments()

    return render_template("comment.html", comments = comments,pitch = pitch,title = title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user, pitches = pitches)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))