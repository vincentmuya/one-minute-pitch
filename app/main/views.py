from flask import render_template
from . import main
from app.models import Pitches
from flask_login import login_required,login_manager
from app.models import Pitches
from .forms import PitchForm


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
