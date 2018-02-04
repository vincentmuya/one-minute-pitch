from flask import render_template
from app import app
from .requests import get_pitches

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting pickup lines pitches
    pickup_pitches = get_pitches('pickup')
    interview_pitch = get_interview_pitch('interview')
    product_pitch = product_pitch('product')
    promotion_pitch = promotion_pitch('promotion')

    title = 'Home - One Minute Pitch'
    return render_template('index.html', title = title, pickup = pickup_pitches, interview = interview_pitch, product = product_pitch, promotion = product_pitch)
