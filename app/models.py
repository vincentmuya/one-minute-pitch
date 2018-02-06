from . import db

class Pitches:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,id,author,pitch,vote_average,vote_count):
        self.id =id
        self.author = author
        self.pitch = pitch
        self.vote_average = vote_average
        self.vote_count = vote_count

class User(db.Model):
    __tablename__='users'
    id =db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(225))

    def __repr__(self):
        return f'User{self.username}'

class Role(db.Model):
    __table__='roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(225))

    def __repr__(self):
        return f'User{self.name}'
