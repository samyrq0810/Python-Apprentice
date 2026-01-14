from guizero import *

first_num = 0
second_num = 0
operation = ""

def enterbutton_push():
    global firstnumtextbox
    global secondnumtextbox

    return firstnumtextbox.value + secondnumtextbox.value



app = App(title = "calculator", layout = "grid", height=500, width=500)

firstnumtextbox = TextBox(app, width=350, grid=[1,3])
secondnumtextbox = TextBox(app, width=350, grid=[1,6])
enterbutton = PushButton(app, text="Enter", grid=[0,0], command=print(enterbutton_push()))
app.display()