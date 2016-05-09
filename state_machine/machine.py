class BaseStateMachine(object):
    def run_all(self, *args, **kwargs):
        assert False, 'run_all not implemented'


class StateMachine(BaseStateMachine):
    def __init__(self, current_state):
        self.current_state = current_state
        self.current_state.run()

    def run_all(self, inputs, verbose=False):
        for input_state in inputs:
            if verbose:
                print(input_state)
            self.current_state = self.current_state.next(input_state)
            self.current_state.run()
