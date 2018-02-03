def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - One Minute Pitch'
    return render_template('index.html', title = title)
