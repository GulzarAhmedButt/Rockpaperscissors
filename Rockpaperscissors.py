import random

choices = ['Rock','Paper','Scissors']

player_score = 0
computer_score = 0

player = False

random.seed()


while True:
    player = input('Rock,Paper or Scissors? ').capitalize()
    computer = random.choice(choices)
    if player == computer:
        print('TIE!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You Lose!',computer,'covers',player)
            computer_score+=1
        else:
            print('You Win!',player,'smashes',computer)
            player_score +=1
    elif player == 'Paper':
        if computer == 'Scissors':
            print('You Lose!',computer,'cuts',player)
            computer_score+=1
        else:
            print('You Win!',player,'covers',computer)
            player_score +=1
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You Lose!',computer,'smashes',player)
            computer_score+=1
        else:
            print('You Win!',player,'cuts',computer)
            player_score +=1
    elif player == 'End':
        print('Final Scores')
        print('Computer Score: {}'.format(computer_score))
        print('Player Score: {}'.format(player_score))
        break
