from menu import *

class Room:
    def __init__(self, room_number, room_type, room_price):
       self.room_number = room_number
       self.room_type = room_type
       self.room_price = room_price
    
    def describe(self):
        return f"{self.room_number}"
