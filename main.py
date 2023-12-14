import random

print('Welcome to Rock, Paper, Scissors!')
playerChoice = int(input('What do you choose? Type "0" for Rock, "1" for Paper, and "2" for Scissors.\n'))
a, b, c = 'rock', 'paper', 'scissors'
print('You chose ' + str(playerChoice))
pcChoice = random.randint(0,2)
print('Computer chose ' + str(pcChoice))
if playerChoice == pcChoice:
    print('Draw! Game over. ')
elif playerChoice == 0 and pcChoice == 2:
    print('You win! Game over. ')
elif playerChoice == 1 and pcChoice == 0:
    print('You win! Game over. ')
elif playerChoice == 2 and pcChoice == 1:
    print('You win! Game over. ')
elif pcChoice == 0 and playerChoice == 2:
    print('You lose! Game over. ')
elif pcChoice == 1 and playerChoice == 0:
    print('You lose! Game over. ')
elif pcChoice == 2 and playerChoice == 1:
    print('You lose! Game over. ')
else:
    print('Something went wrong')