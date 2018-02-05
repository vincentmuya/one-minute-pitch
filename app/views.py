from flask import render_template
from app import app
from app.models import pitches

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting pickup lines pitches
    # def get_pitches(category):
        # pickup_pitches = get_pitches()
        # print(pickup_pitches)

    # title = 'Home - One Minute Pitch'
    return render_template('index.html')
