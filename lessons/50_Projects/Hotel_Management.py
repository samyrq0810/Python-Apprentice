"""
if needed later on, check in rooms are in this order: [room type, number of days, cost].

!!## kind of redoed the checkout funt in class room, may not work ##!!
"""

from guizero import *
import time

bank = 50000
numOfEmptyRoom = 25
x = 0
days = 0

while x < 10:
    last_time = time.time

    if time.time() - last_time > 5:
        days = days + 1
        last_time = time.time()
        x = x + 1
    



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
        print(f"{self.guestName} has booked room number {self.roomNumber} for {numDays} days")

    def checkout(self):
        global days
        while days < self.numDays:
            pass

        print(f"{self.guestName} has check out of room number {self.roomNumber}")
        self.isAvailable = True
        numOfEmptyRoom = numOfEmptyRoom + 1


rooms = [Room(125, i + 1) for i in range(25)]




app = App(title="Hotel Management", layout="grid", height=400, width=400)

box1 = Box(app, width=200, height=100, grid=[0,0], border=True)
box2 = Box(app, width=200, height=100, grid=[1,0], border=True)

numOfEmptyRooms = Text(box1, text=f"Number of empty rooms: {numOfEmptyRoom}")



rooms[1].book("zxc",1)
rooms[2].book("jh",2)
rooms[3].book("sd",3)
rooms[4].book("dgh",4)
rooms[5].book("ew",5)
rooms[6].book("qw",6)






app.display()




