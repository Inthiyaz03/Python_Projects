import random

user_choice = input("Do you want to play a game me with y/n ").lower()
options = ["rock","paper","scissors"]
user_wins , computer_wins = 0,0

if user_choice == 'n':
    print("OK bye...!")
    exit

else:

    while True:
        user_input = input("Type rock,paper,scissors or q to quit ").lower()
        if user_input == 'q':
            break
        if user_input not in options:
            continue

        computer_input = random.randint(0,2)
        #rock = 0, paper=1,scissors=2
        computer_choice = options[computer_input]
        print("computer picked ",computer_choice," so " ,end=" ")

        if user_input == options[0] and computer_choice == options[1]:
            print("you won")
            user_wins+=1
        elif user_input== options[2] and computer_choice==options[1]:
            print("you won")
            user_wins+=1
        elif user_input==options[1]  and computer_choice==options[0]:
            print("you won")
            user_wins+=1
        else:
            print("you lost")
            computer_wins+=1

print("you won ", user_wins," times with me")
print("you lost",computer_wins," times with me")
