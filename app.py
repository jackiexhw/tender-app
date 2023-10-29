from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm
# from cockroachdb.sqlalchemy import run_transaction

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)


### MODELS ###
class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column('room_id', db.Integer, primary_key=True)
    status = db.Column(db.Integer)

    def __init__(self, id):
        self.id = id
        self.status = 0


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column('player_id', db.Intger, primary_key=True)

    def __init__(self, id):
        self.id = id


# Junction table btw players and rooms (many to one)
class PlayerRoom(db.Model):
    __tablename__ = 'player_rooms'
    player_id = db.Column('player_id', db.Integer, primary_key=True)
    room_id = db.Column('room_id', db.Integer)

    def __init__(self, player_id, room_id):
        self.player_id = player_id
        self.room_id = room_id


##############

@app.get("/register_new_device")
def register_new_device():
    # Database lookup, find the smallest unique number
    smallest = session.query(Player).order_by(Player.id.desc())
    
    # Add new player to the database (give new player a unique id)
    new_id = smallest_unique + 1
    
    return str(smallest)

@app.get("/create_room/<player_id>")
def create_room(player_id):
    # Get the smallest unique value for a room
    smallest_unique_room_id = 100

    # Increment the value and store into the database
    current_id = smallest_unique_room_id + 1

    # Store the current player_id into the player_rooms table


    return current_id

@app.get("/register_device_in_room/<player_id>/<room_id>")
def register_device_in_room(player_id, room_id):
    return {"p":player_id, "r":room_id}


@app.get("/start_room/<room_id>")
def start_room(room_id):
    # Set the STARTED flag to be true in the rooms table

    return "Success", 200

@app.get("/get_status/<room_id>")
def get_status(room_id):
    # Get the current status of the room in the rooms table

    return 200