# give a random choice from options given
from random import choice
option = ["Heads", "Tails"]
computerMove = choice(option)
print("The computer chose: " + computerMove)
# to chossen from some numbers inclusive
from random import randint
number = randint(1, 20)
print(number)
#randomly shuffle a list
from random import shuffle
cards = shuffle(["Jack", "Queen", "King"])

print(cards)

# to import statistics module
import statistics
print(statistics.mean([98, 75, 56, 57, 89, 78, 91, 85]))
