
import random


class RPS():
    def __init__(self):
        self.rps = ["rock", "paper", "scisor"]


    def get_compute_choice(self):
        return print(random.choice(self.rps))


if __name__=="__main__":
    game= RPS()
    game.get_compute_choice()
