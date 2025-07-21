import random

print("===================")
print("Rock Paper Scissors")
print("===================")

1 == "✊"
2 == "✋"
3 == "✌️"

print("1) Rock")
print("2) Paper")
print("3) Scissors")


player_input = int(input("Pick a Number: "))
cpu_input = random.randint(1,3)

print(player_input)
print(cpu_input)

if player_input == cpu_input:
    print('Its a tie. Try again...')
else:
    pass

if player_input == 1 and cpu_input == 2 and cpu_input != 3:
    print('You lost! - Try again...')
else:
    pass 

if player_input == 2 and cpu_input == 1 and cpu_input != 3: 
    print('You won!')
else: 
    pass

if player_input == 3 and cpu_input == 2 and cpu_input != 1:
    print("You won!")

else:
    pass
