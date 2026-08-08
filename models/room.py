from menu import *

class Room:

    total_rooms = 40
    occupied_rooms = 0
    revenue = 0
    

    def __init__(self, room_number, room_type, room_price):
       self.room_number = room_number
       self.room_type = room_type
       self.room_price = room_price
       Room.occupied_rooms +=1
       Room.total_rooms -= 1

       
    
    def describe(self):
        return f"{self.room_number}"
        
    def total_revenue(self):
        return f"{Room.revenue + self.room_price}"