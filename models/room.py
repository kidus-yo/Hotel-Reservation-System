from menu import *

class Room:

    total_room = 0
    def __init__(self, room_number, room_type, room_price):
       self.room_number = room_number
       self.room_type = room_type
       self.room_price = room_price
       Room.total_room +=1
    
    def describe(self):
        return f"{self.room_number}"
