from flask import Flask

app = Flask(__name__)

@app.get("/register_new_device")
def register_new_device():
    # Database lookup, find the smallest unique number
    smallest_unique = 4
    
    # Add new player to the database (give new player a unique id)
    new_id = smallest_unique + 1
    
    return str(new_id)

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