"""
if needed later on, check in rooms are in this order: [room type, number of days, cost].
"""

import random

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


print(check_in())


    