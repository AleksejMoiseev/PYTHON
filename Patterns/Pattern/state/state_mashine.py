from transitions import Machine
import random


class Superhero(object):

    states = ['asleep', 'hanging out', 'hungry', 'sweaty', 'saving the world']

    def __init__(self, name):
        self.name = name
        self.kittens_rescued = 0
        # Initialize the state machine
        self.machine = Machine(model=self, states=Superhero.states, initial='asleep')

        # Add some transitions.
        self.machine.add_transition(trigger='wake_up', source='asleep', dest='hanging out')
        self.machine.add_transition('work_out', 'hanging out', 'hungry')
        self.machine.add_transition('eat', 'hungry', 'hanging out')

        self.machine.add_transition('distress_call', '*', 'saving the world',
                         before='change_into_super_secret_costume')

        # When they get off work, they're all sweaty and disgusting. But before
        # they do anything else, they have to meticulously log their latest
        # escapades. Because the legal department says so.
        self.machine.add_transition('complete_mission', 'saving the world', 'sweaty',
                         after='update_journal')

        # Sweat is a disorder that can be remedied with water.
        # Unless you've had a particularly long day, in which case... bed time!
        self.machine.add_transition('clean_up', 'sweaty', 'asleep', conditions=['is_exhausted'])
        self.machine.add_transition('clean_up', 'sweaty', 'hanging out')

        self.machine.add_transition('nap', '*', 'asleep')

    def update_journal(self):
        self.kittens_rescued += 1

    @property
    def is_exhausted(self):
        exhausted = random.random() < 0.5
        print('!!!!!!!!!!', exhausted)
        return exhausted

    def change_into_super_secret_costume(self):
        print("Красота?")


if __name__ == '__main__':
    batman = Superhero("Batman")
    # Начальное состояние
    print(batman.state)
    batman.wake_up()
    print(batman.state)
    # batman.clean_up()
    batman.distress_call()
    print(batman.state)
    batman.complete_mission()
    print(batman.state)
    batman.clean_up()
    print(batman.state)

