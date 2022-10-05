
import random


class RPS():
    def __init__(self):
        self.rps = ["rock", "paper", "scissor"]

    def get_compute_choice(self):
        """Get computer's choice
        :return: string: computers choice"""

        computer_choice = random.choice(self.rps)
        print(computer_choice)
        return computer_choice

    def get_user_choice(self):
        """Get users choice
        :return: string: from users input"""

        user_choice = input("Type choose rock, paper or scisors: ")
        if user_choice.lower() not in self.rps:
            print("You did not enter a valid value for the game")
            user_choice = input("Please enter one of the following to play the game Rock, Paper or Scissor: ")
        return user_choice.lower()

    def game_flow(self, user_choice, computer_choice):
        """Game flow architecture
        :user_choice: string: input from another function
        :computer_choice:string: input from another function"""

        if user_choice == "rock" and computer_choice == "scissor":
            return True
        if user_choice == "paper" and computer_choice == "rock":
            return True
        if user_choice == "scissor" and computer_choice == "paper":
            return True
        else:
            return False

    def still_play(self):
        """Function to check if the user still want to play
        :return: bool: True or False"""

        _continue_playing = input("Do you still want to continue playing? Type yes or no: ")
        if "yes" in _continue_playing.lower():
            return True
        else:
            return False
    
    def get_winner(self):
        """Decision check who won and print"""
        user_choice = self.get_user_choice()
        computer_choice = self.get_compute_choice()
        win = self.game_flow(user_choice, computer_choice)
        if win:
            print("Congratualtions, you won!")
        else:
            print("I am sorry but you lost")
        
        
    def play(self):
        """Function to loop through games if the user wants to keep playing"""
        _continue=True
        while(_continue):
            self.get_winner()
            _continue = self.still_play()





if __name__=="__main__":
    game= RPS()
    game.play()

