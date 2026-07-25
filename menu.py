from models.room import * 
from database import *

def main_menu():
    print("-" * 30)
    print("========KIDUS GRAND HOTEL🏩=========")
    print("-" * 30)
    print("WELCOME💐")
    print("=Main Menu=")
    print("1. Add Room")
    print("2. View Room")
    print("3. Remove Room")
    print("4. Book Room")
    print("5. Cancel Reservation")
    print("6. View Reservation")
    print("7. Search Customer")
    print("8. Hotel Statstics")
    print("9. Exit❌")

    choice = int(input("Enter your choice: "))
    return choice


def add_room():

    print("*" * 30)
    print("Room Registration®️")
    print("*" * 30)

    room_number = int(input("Enter a room number: "))
    room_type = input("Enter Room Type: ")
    room_price = float(input("Enter room price: "))

    room = Room(room_number, room_type, room_price)
    rooms.append(room)


def view_room():

    print("*" * 30)
    print("Registered Room🛏️")
    print("*" * 30)

    for room in rooms:
        print("_" * 30)
        print(f"Room Number: {room.room_number}")
        print(f"Room Type: {room.room_type}")
        print(f"Room Price: {room.room_price:.2f}$")
        print("_" * 30)


    
