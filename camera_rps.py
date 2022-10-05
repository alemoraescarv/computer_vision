
import cv2
from keras.models import load_model
import numpy as np
import time
import random



class RPS():


    def __init__(self):
        self.computer_choice = ["rock", "paper", "scissor"]
        self.max_seconds_choose = 10
        self.computer_wins = 0
        self.user_wins = 0
        self.rounds = 0
        self.labels = ["scissors", "rock", "paper", "nothing"]

    def get_computer_choice(self):
        """Get computer's choice
        :return: string: computers choice"""
        computer_choice = random.choice(self.computer_choice)
        print("Computer choice is :{}".format(computer_choice))
        return computer_choice
    
    def get_prediction(self, prediction):
        """Get predictions from model, highest value in the array
        :prediction: string : list with the numbers for each label
        :return: prediction identified by the model"""
        max_arg_index = np.argmax(prediction)
        print("Your choice iss : {}".format(self.labels[max_arg_index]))
        return self.labels[max_arg_index]

    def get_user_choice(self):
        """Get user's choice, gitve the user 6seconds to choose. If didntm choose increase the count
        :return: string: 
        """
        model = load_model('converted_keras/keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        total_duration = 6
        time_passed = 0
        start_time = time.time()

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            
            if cv2.waitKey(1) &  0xFF == ord('q'):
                break
            if time.time() - start_time > total_duration:
                print("6 seconds have passed, time it over to choose")
                if self.get_prediction(prediction) != "Nothing":
                    print(prediction)
                    break   
                else:
                    print("You didnt choose yet")
                    continue
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return self.get_prediction(prediction) 

    def game_flow(self, user_choice, computer_choice):
        """Game flow architecture
        :user_choice: string: input from another function
        :computer_choice:string: input from another function"""

        if user_choice == "rock" and computer_choice == "scissor":
            self.user_wins +=1
            #return self.user_wins
        if user_choice == "paper" and computer_choice == "rock":
            self.user_wins +=1
            #return self.user_wins
        if user_choice == "scissor" and computer_choice == "paper":
            self.user_wins +=1
            #return self.user_wins
        elif user_choice != computer_choice:
            self.computer_wins +=1
            #return self.computer_wins

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
        computer_choice = self.get_computer_choice()
        self.game_flow(user_choice, computer_choice)
        if self.user_wins >= 3:
            print("Congratualtions, you won! The score was {} for you against {} for the computer".format(self.user_wins, self.computer_wins))
            return False
        elif self.computer_wins >= 3:
            print("You lost the computer won! The score was {} for you against {} for the computer".format(self.user_wins, self.computer_wins))
            return False
        else:
            return True
            print("This is round number {}. Let's continue".format(self.rounds))

    def play(self):
        """Function to loop through games if the user wants to keep playing"""
        _continue=True
        while(_continue):
            self.rounds +=1
            _continue = self.get_winner()


if __name__=="__main__":
    game = RPS()
    game.play()