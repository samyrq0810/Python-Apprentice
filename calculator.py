from guizero import *

first_num = 0
second_num = 0
operation = ""



app = App(title = "calculator", layout = "grid")

button0 = PushButton(app, text="0", grid=[2,3], command=)
button1 = PushButton(app, text="1", grid=[1,0])
button2 = PushButton(app, text="2", grid=[2,0])
button3 = PushButton(app, text="3", grid=[3,0])
button4 = PushButton(app, text="4", grid=[1,1])
button5 = PushButton(app, text="5", grid=[2,1])
button6 = PushButton(app, text="6", grid=[3,1])
button7 = PushButton(app, text="7", grid=[1,2])
button8 = PushButton(app, text="8", grid=[2,2])
button9 = PushButton(app, text="9", grid=[3,2])

buttonAdd = PushButton(app, text="+", grid=[4,0])
buttonSub = PushButton(app, text="-", grid=[4,1])
buttonMult = PushButton(app, text="x", grid=[4,2])
buttonDiv = PushButton(app, text="÷", grid=[4,3])

app.display()