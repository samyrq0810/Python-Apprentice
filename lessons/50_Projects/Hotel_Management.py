"""
if needed later on, check in rooms are in this order: [room type, number of days, cost].
"""

import random
from guizero import App, Text, PushButton, Slider, Box

roomStandardNum = 0
roomLuxuryNum = 0
roomSuiteNum = 0

Bank = 10000

def room_type():
    Room_Type_Numify = random.randint(0, 3)
    Room_Type = ""

    if Room_Type_Numify == 0:
        Room_Type = "Standard"
    elif Room_Type_Numify == 1:
        Room_Type = "Luxury"
    else:
        Room_Type = "Suite"
        
    return Room_Type

def number_of_days():
    Num_of_days = random.randint(1, 6)

    return Num_of_days

def cost(room_type, number_of_days):
    cost = 0
    if room_type == "Standard":
        cost = 100
    elif room_type == "Luxury":
        cost = 150
    elif room_type == "Suite":
        cost = 200
    
    cost = cost * number_of_days

    return cost
        
def check_in():
    roomType = room_type()
    numberOfDays = number_of_days()
    Cost = cost(roomType, numberOfDays)
    checkIn = []

    checkIn.append(roomType)
    checkIn.append(numberOfDays)
    checkIn.append(Cost)

    return checkIn

def build_standard(money):
    cost = 2000
    if money > cost:
        roomStandardNum = roomStandardNum + 1
        money = money - 2000

def build_luxury(money):
    cost = 3000
    if money > cost:
        roomLuxuryNum = roomLuxuryNum + 1
        money = money - 3000

def build_suite(money):
    cost = 4000
    if money > cost:
        roomSuiteNum = roomSuiteNum + 1
        money = money - 4000

app = App(title = "hotel management", layout = "grid")
standardBox = Box(app, border = True, grid = [0,0])
standard_room = Text(standardBox, text="number of standard rooms")
luxury_room = Text(app, text="number of luxury rooms", grid = [1,0])

luxuryBox = Box(app, border = True, grid = [3,0])
app.display()

