from models.customer import *
from models.room import *

class Reservation(Room, Customer):
    def __init__(self, reservation_id):
      self.reservation_id = reservation_id
      
reservation = Reservation()    