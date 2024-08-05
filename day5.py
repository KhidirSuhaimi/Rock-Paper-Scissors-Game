import random
computer_choice = random.randint(0,2)
choice = -1
while choice > 2 or choice < 0:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
    if choice >2 or choice < 0:
        print("Enter the correct number, dumbass!")


actual = ''
actual_Computer =''

if choice == 0:
    actual = 'Rock'
elif choice == 1:
    actual = 'Paper'
elif choice == 2:
    actual = 'Scissors'
print(f"You chose {actual}")


if computer_choice == 0:
    actual_Computer = 'Rock'
elif computer_choice == 1:
    actual_Computer = 'Paper'
elif computer_choice == 2:
    actual_Computer = 'Scissors'

print(f"Computer chose: {actual_Computer}")
if choice == 0 and computer_choice == 0:
    print("It is a draw")
elif choice == 0 and computer_choice == 1:
    print("Paper beats Rock, Computer Wins!")
elif choice == 0 and computer_choice == 2:
    print("Rock beats Scissors, You Win!")
elif choice == 1 and computer_choice == 0:
    print("Paper beats Rock, You Win!")
elif choice == 1 and computer_choice == 1:
    print("It is a draw")
elif choice == 1 and computer_choice == 2:
    print("Scissors beat Paper, Computer Wins!")
elif choice == 2 and computer_choice == 0:
    print("Rock beats Scissors, Computer Wins!")
elif choice == 2 and computer_choice == 1:
    print("Scissors beats Paper, You Win!")
elif choice == 2 and computer_choice == 2:
    print("It is a draw")
