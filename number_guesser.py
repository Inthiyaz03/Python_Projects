import random

gamer_choice = str(input("Do you want start the game: y/n ")).lower() 

if gamer_choice == "y":

    top_of_range = input("Enter a number: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("Please type a number which is greater than zero next time !")
            quit()
    else: 
        print("Please type a number next time")
        quit()

    random_num = random.randint(0,top_of_range)
    Guesses = 0
    while True:
        Guesses+=1
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess=int(user_guess)
        else:
            print("Please type a number next time.!")
            continue

        if user_guess==random_num:
            print("you got it")
            break
        elif user_guess>random_num:
            print("You were above the number")
        else:
            print("you were below the number")

    print("You got it in ",Guesses, " guesses congratulations..!")

else:
    print("Bye..see you next time..!")