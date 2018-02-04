from app import app
from .models import pitch

Pitch = pitch.Pitch

# Getting pitch
pitch = app.config['PITCH']


def get_pitches(category):
    '''
    Function that gets the pitch response request
    '''
    get_pitches = format(category)

    pitch_results = None

    if get_pitches_response['results']:
        pitch_results_list = get_pitches_response['results']
        pitch_results = process_results(pitch_results_list)

def process_results(pitch_list):
    '''
    Function  that processes the pitch result and transform them to a list of Objects

    Args:
        pitch_list: A list of dictionaries that contain pitch details

    Returns :
        pitch_results: A list of pitch objects
    '''
    pitch_results = []
    for pitch_item in pitch_list:
        id = pitch_item.get('id')
        author = pitch_item.get('original_title')
        pitch = pitch_item.get('pitch_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if pitch:
            pitch_object = Pitch(id,author,pitch,vote_average,vote_count)
            pitch_results.append(pitch_object)

    return pitch_results
