States = []

class state:
    def __init__(self, state_name, state_id, start_func):
        self.state_name = state_name
        self.state_id = state_id
        self.start_func = start_func

class frame:
    def defaultMenu():
        print("This is default menu. Please customise your menu")

    def __init__(self, menu_func = defaultMenu):
        self.state_amount = 0
        self.addState("Main menu",  menu_func)
        self.curr_state = 0

    def addState(self, state_name, state_func):
        self.state_amount += 1
        States.append(state(state_name, self.state_amount, state_func))

    def frameUpdate(self, next_state_id = 0):
        self.curr_state = next_state_id
        return self.frameFunc()

    def frameFunc(self):
        return States[int(self.curr_state)].start_func()

