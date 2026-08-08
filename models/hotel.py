from models.reservation import *
from models.customer import *
from models.room import *


class Hotel:
    def __init__(self, room, customer, reservation):
        self.room = room
        self.customer = customer
        self.reservation = reservation