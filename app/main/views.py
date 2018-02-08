from flask import render_template,request,redirect,url_for,abort
from . import main
from app.models import Pitches
from flask_login import login_required,login_manager
from app.models import Pitches
from .forms import PitchForm,UpdateProfile


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - One Minute Pitch'
    return render_template('index.html', title = title)

@main.route('/pitch/new/',methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        new_pitch = Pitch(pitch.id,author,pitch)
        new_pitch.save_pitch()
        return redirect(url_for('pitch'))
    return render_template('new_pitch.html',pitch_form=form)

@main.route('/user/<username>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is none:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',method = ["GET","POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is none:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)
