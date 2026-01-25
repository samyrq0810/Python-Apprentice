"""
if needed later on, check in rooms are in this order: [room type, number of days, cost].

!!## kind of redoed the checkout funt in class room, may not work ##!!
"""

from guizero import *
import time

bank = 67
numOfEmptyRoom = 25

    



class Room:
   
    def __init__(self, cost:int, roomNumber:int):
        """Initializes a new Person object."""

        self.cost = cost
        self.isAvailable = True
        self.roomNumber = roomNumber
        self.guestName = ""
        self.numDays = 0

  
    def book(self, guestName:str, numDays:int):
        global bank
        global numOfEmptyRoom
        self.isAvailable = False
        self.numDays = numDays
        bank = bank + numDays * self.cost
        self.guestName = guestName
        numOfEmptyRoom = numOfEmptyRoom - 1
        print(f"{self.guestName} has booked room number {self.roomNumber} for {numDays} days.")

    def checkout(self):
        global numOfEmptyRoom
        last_time = time.time()
        days = 0

        while days < self.numDays:
            if time.time() - last_time > 5:
                days = days + 1
                last_time = time.time()

        numOfEmptyRoom = numOfEmptyRoom + 1

        print(f"{self.guestName} is checked out of room number {self.roomNumber}.")







rooms = [Room(125, i + 1) for i in range(25)]

print("Asdf")

rooms[0].book("zxc",1)
print(bank)
print(numOfEmptyRoom)
rooms[1].book("jh",2)
print(bank)
print(numOfEmptyRoom)
rooms[2].book("sd",3)
print(bank)
print(numOfEmptyRoom)
rooms[3].book("dgh",4)
print(bank)
print(numOfEmptyRoom)
rooms[4].book("ew",5)
print(bank)
print(numOfEmptyRoom)
rooms[5].book("qw",6)



rooms[0].checkout()
print(numOfEmptyRoom)
rooms[1].checkout()
print(numOfEmptyRoom)
rooms[2].checkout()
print(numOfEmptyRoom)
rooms[3].checkout()
print(numOfEmptyRoom)
rooms[4].checkout()
print(numOfEmptyRoom)
rooms[5].checkout()
print(numOfEmptyRoom)

app.display()







