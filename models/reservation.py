from models.customer import *
from models.room import *
from database import *

class Reservation():
 
    reservation_ID = 1101     
    def __init__(self, check_in, check_out, room_number):
        self.check_in = check_in
        self.check_out = check_out
        Reservation.reservation_ID+=1

        self.room = Room(room_number)
        self.customer = Customer()
     
    def reserve_id(self):
         return f"{self.reservation_ID}"
      

