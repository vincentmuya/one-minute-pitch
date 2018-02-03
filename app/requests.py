from app import app
from .models import pitch

Pitch = pitch.Pitch

def get_pitches(category):
    '''
    Function that gets the pitch response request
    '''
    get_pitches = format(category)

        pitch_results = None

        if get_pitchs_response['results']:
            pitch_results_list = get_pitchs_response['results']
            pitch_results = process_results(pitch_results_list)


    return pitch_results
