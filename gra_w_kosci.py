from random import randint 

min = 1
max = 6

player_1_points = 0
player_2_points = 0

def dice_throw(tries: int):
    sum = 0
    for i in range(0, tries):
        throw = randint(min, max)
        sum += throw
    return sum

print("Welcome to the game!!! Each player will have 2 dice rolls. Win the one who gets more points. Good luck and have fun")
tries = int(input("Choose number of throws in each turn.\n"))
rounds = int(input("Choose number of rounds.\n"))

turn = 0

while turn < rounds:
    player_1_points += dice_throw(tries)
    player_2_points += dice_throw(tries)

    turn += 1
    


print(f'Player1 throw, the sum of the points is {player_1_points}')
print(f'Player2 throw,the sum of the points is {player_2_points}')

if player_1_points > player_2_points:
    print("Player1 wins this round")
    
elif player_1_points < player_2_points:
    print("Player2 wins this round")

else:
    print("Draw!!!")
