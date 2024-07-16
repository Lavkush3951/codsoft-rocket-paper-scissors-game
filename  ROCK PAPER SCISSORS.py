import random
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "paper vs scissor - scissor win\n"
      + "scissor vs rock -rock win \n"
      + "rock vs paper - paper win \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")


    choice = int(input("Enter your choice :"))
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺'))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

    
    compter_choice = random.randint(1, 3)

    while compter_choice == choice:
        compter_choice = random.randint(1, 3)

    if compter_choice == 1:
        compter_choice_name = 'RocK'
    elif compter_choice == 2:
        compter_choice_name = 'Paper'
    else:
        compter_choice_name = 'Scissors'
    print("Computer choice is \n", compter_choice_name)
    print(choice_name, 'Vs', compter_choice_name)
    # we need to check of a draw
    if choice == compter_choice:
        print('Its a Draw')
        result = "DRAW"
    # condition for winning
    if (choice == 1 and compter_choice == 2):
        print('paper cover the rock \n')
        result = 'Paper'
    elif (choice == 2 and compter_choice == 1):
        print('paper cover the rock\n ')
        result = 'Paper'

    if (choice == 1 and compter_choice == 3):
        print('Rock damage the scissor \n')
        result = 'Rock'
    elif (choice == 3 and compter_choice == 1):
        print('Rock damage the scissor \n')
        result = 'RocK'

    if (choice == 2 and compter_choice == 3):
        print('Scissors cuts the paper\n ')
        result = 'Scissors'
    elif (choice == 3 and compter_choice == 2):
        print('Scissors cuts the paper \n')
        result = 'Rock'
    if result == 'DRAW':
        print(" Its a tie ")
    if result == choice_name:
        print("you win")
    else:
        print(" Computer win")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
    print(result)
