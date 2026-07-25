from menu import *

class Room:
    def __init__(self, room_number, room_type, room_price):
       self.room_number = room_number
       self.room_type = room_type
       self.room_price = room_price
    def get_info(self):
        print(f"Room Number: {self.room_number}")
        print(f"Room Type: {self.room_type}")
        print(f"Room Price: {self.room_price}")
 
