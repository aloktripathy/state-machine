from state_machine.state import State
from state_machine.machine import StateMachine


class MouseAction:
    """Class representing an action performed by the mouse"""
    def __init__(self, action):
        self.action = action

    def __hash__(self):
        return hash(self.action)

    def __eq__(self, other):
        return self.action == other.action

    def __str__(self):
        return 'action: ' + self.action


class WaitingState(State):
    def run(self):
        print("Waiting: Broadcasting cheese smell")


class LuringState(State):
    def run(self):
        print("Luring: Presenting Cheese, door open")


class TrappingState(State):
    def run(self):
        print("Trapping: Closing door")


class HoldingState(State):

    def run(self):
        print("HoldingState: Mouse caught")


class ActionSet:
    """All the actions a mouse can perform"""
    appears = MouseAction('appears')
    runs_away = MouseAction("mouse runs away")
    enters = MouseAction("mouse enters trap")
    escapes = MouseAction("mouse escapes")
    trapped = MouseAction("mouse trapped")
    removed = MouseAction("mouse removed")


class StateSet:
    waiting = WaitingState()
    luring = LuringState()
    trapping = TrappingState()
    holding = HoldingState()

# Declare state transition rules
StateSet.waiting.transitions = {
    ActionSet.appears: StateSet.luring
}

StateSet.luring.transitions = {
    ActionSet.runs_away: StateSet.waiting,
    ActionSet.enters: StateSet.trapping
}

StateSet.trapping.transitions = {
    ActionSet.escapes: StateSet.waiting,
    ActionSet.trapped: StateSet.holding
}

StateSet.holding.transitions = {
    ActionSet.removed: StateSet.waiting
}

if __name__ == "__main__":
    inputs = [
        ActionSet.appears,
        ActionSet.runs_away,
        ActionSet.enters,
        ActionSet.runs_away,
        ActionSet.appears,
        ActionSet.enters,
        ActionSet.trapped,
        ActionSet.removed,
        ActionSet.appears,
        ActionSet.runs_away,
        ActionSet.escapes,
        ActionSet.appears,
        ActionSet.enters,
        ActionSet.trapped,
        ActionSet.removed,
    ]
    mouse_trap = StateMachine(StateSet.waiting)
    mouse_trap.run_all(inputs, verbose=True)
