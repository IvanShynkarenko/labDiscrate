import random
import networkx as nx
import matplotlib.pyplot as plt
class State:
    SLEEP = "Sleep"
    EAT = "Eat"
    WORK = "Work"
    REST = "Rest"
    TRAIN = "Train"
    INSOMNIA = "Insomnia"
    SHOCK = "Shock"

class DailyRoutine:
    def __init__(self):
        self.state = State.SLEEP
        self.energy = 100
        self.hunger = 0 

    def handle_random_event(self):
        event = random.choice(["Unexpected call", "Visit from a friend", "Feeling unwell"])
        if event == "Unexpected call":
            if self.state != State.SLEEP:
                print("Got an unexpected call!")
                self.state = State.SHOCK
        elif event == "Visit from a friend":
            if self.state != State.SLEEP:
                print("Friend visited unexpectedly!")
                self.state = State.REST
        elif event == "Feeling unwell":
            print("Feeling unwell...")
            if self.state == State.SLEEP:
                print("Having insomnia...")
                self.state = State.INSOMNIA

    def handle_hour(self, hour):
        if hour == 7:
            self.state = State.SLEEP
        elif hour == 8:
            self.state = State.EAT
        elif hour == 9:
            self.state = State.WORK
        elif hour == 13:
            self.state = State.EAT
        elif hour == 18:
            self.state = State.WORK
        elif hour == 19:
            if self.energy > 60:
                self.state = State.TRAIN
            else:
                self.state = State.REST
        elif hour == 20:
            self.state = State.REST
        elif hour == 22:
            self.state = State.SLEEP

        self.handle_state(hour)

    def handle_state(self, hour):
        if self.energy < 20:
            self.energy += 30
            self.state = State.SLEEP
        elif self.hunger > 80:
            self.hunger -= 30
            self.state = State.EAT
        elif self.state == State.SLEEP:
            self.energy += 20
        elif self.state == State.EAT:
            self.energy += 10
            self.hunger -= 20
        elif self.state == State.WORK:
            if self.energy < 30:
                print(f"Too exhausted! Going home to sleep...")
                self.state = State.SLEEP
            else:
                self.energy -= 20
                self.hunger += 10
        elif self.state == State.TRAIN:
            self.energy -= 40
            self.hunger += 20
        elif self.state == State.REST:
            self.energy += 30
        elif self.state == State.INSOMNIA:
            self.energy -= 50
        elif self.state == State.SHOCK:
            self.energy -= 10
            self.hunger += 10

        self.energy = max(0, min(100, self.energy))
        self.hunger = max(0, min(100, self.hunger))

        print(f"Hour {hour}: {self.state}. Energy: {self.energy}. Hunger: {self.hunger}")

routine = DailyRoutine()

for hour in range(24):
    routine.handle_hour(hour)
    if random.random() < 0.2:
        routine.handle_random_event()

