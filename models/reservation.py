from models.customer import *
from models.room import *
from database import *

class Reservation():
    def __init__(self, reservation_id, check_in, check_out):
        self.reservation_id = reservation_id
        self.check_in = check_in
        self.check_out = check_out

        self.room = Room()
        self.customer = Customer()
     
      
      
reservation = Reservation()
