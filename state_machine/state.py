class BaseState(object):
    def run(self, *args, **kwargs):
        assert False, 'run not implemented'

    def next(self, *args, **kwargs):
        assert False, 'next not implemented'


class State(BaseState):
    transitions = dict()

    def next(self, input):
        """If input has a next state in transition rule then return that state else returns
        current state

        Returns:
            state_machine.state.State
        """
        return self.transitions.get(input, self)

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            return 'State {}'.format(id(self))
