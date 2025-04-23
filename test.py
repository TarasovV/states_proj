from states import frame as fr
from states import state as st

def Menu():
    return input("Input 1 or 2: ")

def Sum():
    print("Summary Func")
    return 0

def Sub():
    print("Substitute func")
    return 0

MainFrame = fr(Menu)
MainFrame.addState("Sum", Sum)
MainFrame.addState("Sub", Sub)

next_state = 0
MainFrame.frameUpdate(next_state)
while True:
    next_state = MainFrame.frameFunc()
    q = input("Type q for exit: ")
    if q == 'q':
        break
    MainFrame.frameUpdate(next_state)
