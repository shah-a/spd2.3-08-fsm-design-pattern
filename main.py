class State:
    def handle_input(self, gumball_machine, input):
        pass


class NoQuarterState(State):
    def handle_input(self, gumball_machine, input):
        if input == 'insert-quarter':
            gumball_machine.state = HasQuarterState()
            print('You inserted a quarter.')
        else:
            print(f'You tried to "{input}". Nothing happened.')


class HasQuarterState(State):
    def handle_input(self, gumball_machine, input):
        if input == 'eject-quarter':
            gumball_machine.state = NoQuarterState()
            print('You ejected a quarter.')
        elif input == 'turn-crank':
            gumball_machine.state = GumballSoldState()
            print('You turned the crank.')
        else:
            print(f'You tried to "{input}". Nothing happened.')


class GumballSoldState(State):
    def handle_input(self, gumball_machine, input):
        if input == 'dispense-gumball':
            gumball_machine.gumball_count -= 1
            if gumball_machine.gumball_count > 0:
                gumball_machine.state = NoQuarterState()
            else:
                gumball_machine.state = OutOfGumballsState()
            print(
                f'You dispensed a gumball. There are {gumball_machine.gumball_count} gumballs left.')
        else:
            print(f'You tried to "{input}". Nothing happened.')


class OutOfGumballsState(State):
    def handle_input(self, gumball_machine, input):
        print('The machine is out of gumballs.')


class GumballMachine:
    def __init__(self):

        self.gumball_count = 5
        self.state = NoQuarterState() if self.gumball_count > 0 else OutOfGumballsState()

    def handle_input(self, input):
        self.state.handle_input(self, input)


gumball_machine = GumballMachine()

gumball_machine.handle_input('insert-quarter')
input()
gumball_machine.handle_input('eject-quarter')
input()
gumball_machine.handle_input('turn-crank')  # should do nothing
input()

gumball_machine.handle_input('insert-quarter')
input()
gumball_machine.handle_input('turn-crank')
input()
gumball_machine.handle_input('dispense-gumball')
input()
