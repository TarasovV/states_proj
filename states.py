States = []

class state:
    def __init__(self, StateName, StateID, StartFunc):
        self.StateName = StateName
        self.StateID = StateID
        self.StartFunc = StartFunc

class frame:
    def DefaultMenu():
        print("This is default menu. Please customise your menu")

    def __init__(self, MenuFunc = DefaultMenu):
        self.StateAmount = 0
        self.add_state("Main menu",  MenuFunc)
        # States.append(state("Main menu",  MenuFunc))
        # print("ADDED  STATE WITH " + str(self.StateAmount) + " ID")
        self.CurrState = 0
        # self.StateAmount += 1

    def add_state(self, StateName, StateFunc):
        self.StateAmount += 1
        States.append(state(StateName, self.StateAmount, StateFunc))
        # print("ADDED  STATE WITH " + str(self.StateAmount) + " ID")
        self.StateAmount += 1

    def frame_update(self, NextStateID = 0):
        self.CurrState = NextStateID

    def frame_func(self):
        # print(States[int(self.CurrState)].StateName)
        # print(str(States[int(self.CurrState)].StateID))
        return States[int(self.CurrState)].StartFunc()

