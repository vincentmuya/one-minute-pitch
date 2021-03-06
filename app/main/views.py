from flask import render_template,request,redirect,url_for,abort
from . import main
from app.models import Pitches,Feedback
from flask_login import login_required,login_manager,current_user
from app.models import Pitches,User
from .forms import FeedbackForm,PitchForm,UpdateProfile
from .. import db,photos


@main.route('/',methods=['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''


    music=Pitches.query.filter_by(category='music').all()
    life=Pitches.query.filter_by(category='life').all()
    pickup=Pitches.query.filter_by(category='pickup').all()
    interview=Pitches.query.filter_by(category='interview').all()
    production=Pitches.query.filter_by(category='production').all()
    promotion=Pitches.query.filter_by(category='promotion').all()

    title = 'Home - One Minute Pitch'
    return render_template('index.html', title = title,life=life,music = music,pickup=pickup,interview=interview,production=production,promotion=promotion)

@main.route('/create/new', methods = ['GET','POST'])
@login_required
def create():
    '''
    View page that returns a form to create your own pitch
    '''
    form = PitchForm()
    if form.validate_on_submit():
        author = form.author.data
        category = form.category.data
        pitch = form.pitch.data
        new_pitch = Pitches(author=author,category=category,pitch=pitch)

        #save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
    title = 'One Minute Pitch'
    music=Pitches.query.filter_by(category='music').all()
    return render_template('new_pitch.html',title=title,pitch_form=form)

@main.route('/feedback/new',methods= ['GET','POST'])
@login_required
def feedback():
    '''
    View page that returns a form to create your own feedback
    '''
    form = FeedbackForm()
    if form.validate_on_submit():
        author = form.author.data
        feedback= form.feedback.data
        new_feedback = Feedback(author=author,feedback= feedback)

        #save feedback methods
        new_feedback.save_feedback()
        return redirect(url_for('main.index'))
    title = 'One Minute Pitch'
    return render_template('new_feedback.html',title= title,feedback_form = form)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
