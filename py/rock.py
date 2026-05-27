# add import of random form the libaries
import random
# create option where the computer can choose randomly from
options = ["Rock", "Paper", "Scissors"]
# create a function to determine the winner of the game
def determine_winner(player, computer, name):
    # determine the winner of the game and print results using the if statement
    if player == computer:
        print(f"{name}, it's a tie!")
    elif (
        (player == "Rock" and computer == "Scissors")
        or (player == "Paper" and computer == "Rock")
        or (player == "Scissors" and computer == "Paper")
    ):
        print(f"{name}, congratulations! You won against the computer.")
    else:
        print(f"{name}, sorry you lost against the computer. Better luck next time!")
    print(f"\nYou played: {player}")
    print(f"Computer played: {computer}")
# ask the user for their name and capitalize the first letter of the name and remove the whitespace using the split method
name = input("Enter your name: ").capitalize().split()[0]
# ask the user if they want to play the game and if they say yes, start the game, otherwise end the program
while True:
    computerMove = random.choice(options)
    playerMove = input(
        "\nEnter your move (Rock, Paper, Scissors): "
    ).capitalize()
    while playerMove not in options:
        print("Invalid move. Please choose Rock, Paper, or Scissors.")
        playerMove = input(
            "Enter your move (Rock, Paper, Scissors): "
        ).capitalize()
    determine_winner(playerMove, computerMove, name)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "no":
        print(f"\nThanks for playing, {name}!")
        break
