"""
if needed later on, check in rooms are in this order: [room type, number of days, cost].
"""

import random
from guizero import *
import time

# roomStandardNum = 0
# roomLuxuryNum = 0
# roomSuiteNum = 0

bank = 50000

# def room_type():
#     Room_Type_Numify = random.randint(0, 3)
#     Room_Type = ""

#     if Room_Type_Numify == 0:
#         Room_Type = "Standard"
#     elif Room_Type_Numify == 1:
#         Room_Type = "Luxury"
#     else:
#         Room_Type = "Suite"
        
#     return Room_Type

# def number_of_days():
#     Num_of_days = random.randint(1, 6)

#     return Num_of_days

# def cost(room_type, number_of_days):
#     cost = 0
#     if room_type == "Standard":
#         cost = 100
#     elif room_type == "Luxury":
#         cost = 150
#     elif room_type == "Suite":
#         cost = 200
    
#     cost = cost * number_of_days

#     return cost
        
# def check_in():
#     roomType = room_type()
#     numberOfDays = number_of_days()
#     Cost = cost(roomType, numberOfDays)
#     checkIn = []

#     checkIn.append(roomType)
#     checkIn.append(numberOfDays)
#     checkIn.append(Cost)

#     return checkIn

# def build_standard(money):
#     cost = 2000
#     if money > cost:
#         roomStandardNum = roomStandardNum + 1
#         money = money - 2000

# def build_luxury(money):
#     cost = 3000
#     if money > cost:
#         roomLuxuryNum = roomLuxuryNum + 1
#         money = money - 3000

# def build_suite(money):
#     cost = 4000
#     if money > cost:
#         roomSuiteNum = roomSuiteNum + 1
#         money = money - 4000



class Room:
   
    def __init__(self, cost:int, roomNumber:int):
        """Initializes a new Person object."""
        self.cost = cost
        self.isAvailable = True
        self.roomNumber = roomNumber
        self.guestName = ""
        self.numDays = 0
        self.isbuilt = False

    def build_new_room():
        x = 100
        global bank
        if bank >= 5000:
            bank = bank - 5000


    def book(self, guestName:str, numDays:int):
        global bank
        self.isAvailable = False
        self.numDays = numDays
        bank = bank + numDays * self.cost
        self.guestName = guestName
        print(f"{self.guestName} has booked room number {self.roomNumber} for {numDays} days")
        
    def check_out(self):
        last_time = time.time()
        days = 0

        while days < self.numDays:
            if time.time() - last_time > 5:
                days = days + 1
                last_time = time.time()

        print(f"{self.guestName} has check out of room number {self.roomNumber}")
        self.isAvailable = True



rooms = [Room(125, i + 1) for i in range(100)]







app = App(title="Hotel Management", layout="grid", height=400, width=400)

box1 = Box(app, width=100, height=300, grid=[0,0], border=True)
box2 = Box(app, width=100, height=300, grid=[1,0], border=True)
box3 = Box(app, width=100, height=300, grid=[2,0], border=True)
box4 = Box(app, width=100, height=300, grid=[3,0], border=True)

box5 = Box(app, width=400, height=100, grid=[0,0], border=True)
box6 = Box(app, width=400, height=100, grid=[0,1], border=True)
box7 = Box(app, width=400, height=100, grid=[0,2], border=True)


app.display()




