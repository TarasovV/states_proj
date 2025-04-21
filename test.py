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
MainFrame.add_state("Sum", Sum)
MainFrame.add_state("Sub", Sub)

NextState = 0
MainFrame.frame_update(NextState)
while True:
    NextState = MainFrame.frame_func()
    # print("Curr state : " + str(MainFrame.CurrState) + " NEXT:" + str(NextState))
    q = input("Type q for exit: ")
    if q == 'q':
        break
    MainFrame.frame_update(NextState)
