""" For this challenge you will create a Rock, Paper, and Scissors game in Python without using any external game libraries.

In the Rock, Paper and Scissors game the goal is to create a command-line game where a user has the option to choose between Rock, Paper and Scissors and if the user wins the score is added, and at the end when the user finishes the game, the score is shown.

The Winning Rules are as follows:

To create the game, you need to take the user’s choice and then you need to compare it with the computer choice which is taken using the random module in Python from a list of choices, and if the user wins then the score will increase by 1.

Test Data:

Enter a choice (Rock(r), Paper(p), Scissors(s)): r

You chose Rock, the computer chose Paper.

Paper covers Rock! You lose.

Play again? (y/n): y
Enter a choice (Rock(r), Paper(p), Scissors(s)): p

You chose Paper, computer chose Paper.

Both players selected Paper. It's a tie!

Play again? (y/n): n
Final Scores:
Computer: 1
Player: 0"""

def player_choose():
    global player_hand
    player_hand = input("Enter a choice (Rock(r), Paper(p), Scissors(s): ")
    if player_hand == "r":
        player_hand = "rock"
    elif player_hand == "p":
        player_hand = "Paper"
    elif player_hand == "s":
        player_hand = "Scissors"
    else:
        print("Try again, using r, s or p")

def computer_choose():
    import random
    global computer_hand
    num = random.randint(1,3)
    if num == 1:
        computer_hand = "Rock"
    elif num == 2:
        computer_hand = "Paper"
    else:
        computer_hand = "Scissors"

def choose():
    player_choose()
    computer_choose()
    print("You chose ", player_hand, ", computer chose ", computer_hand, ".")

