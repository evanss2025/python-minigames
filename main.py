import random
import time

#main function!!
def main():
    while True:
        try:
            user_input = input("Pick a Minigame, your choices are \n Blackjack \n Guess a Number \n Your Choice: ")

            if (user_input == "Blackjack"):
                blackjack()
                break
            elif (user_input == "Guess a Number"):
                guess_a_number()
                break
        
            else:
                print("Please choose a valid minigame")
                pass
        except ValueError:
            print("Please enter a valid answer")
            pass

#main blackjack function
def blackjack():

    print("Welcome to Blackjack!")
    time.sleep(0.8)
    print("Randomizing your cards...")
    user_number = int(random.randint(2, 21))

    time.sleep(0.8)
    print("Your cards add up to", user_number)
    time.sleep(0.8)
    users_choice = input("Would you like to hit or pass? ")
    
    while True:
        try:
            if ((users_choice == "Hit") or (users_choice == "hit")):
                user_number = int(user_number + random.randint(1,12))
                print("Your new number is", user_number)
                time.sleep(1)

                checkNumber(user_number)
  
                break
            elif ((users_choice == "Pass") or (users_choice == "pass")):
                bot_compare(user_number)
                break
            else:
                print("please add a valid input")
                pass

        except ValueError:
            print("Please enter a valid answer")
            pass

#if user wants to hit
def hit(user_number):
    user_number = int(user_number + random.randint(1,12))
    print("Your new number is", user_number)
    time.sleep(1)

    checkNumber(user_number)

#checking number against 21
def checkNumber(user_number):
    while True:
        try:
            if (user_number > 21):
                print("Bust! You lost!")
                break
            elif (user_number == 21):
                print("You got the perfect 21! You automatically win!")
                break
            elif (user_number < 21):
                choice = input("Would you like to hit again? ")

                if ((choice == "Yes") or (choice == "yes")):
                    print("Continuing...")
                    hit(user_number)
                elif (choice == "No"):
                    print("Comparing to bot")

                    bot_compare(user_number)

                    break
                else:
                    print("error")
                    break
                    
                break
            else:
                print("please add a valid input")
                pass

        except ValueError:
            print("Please enter a valid answer")
            pass

#comparing to random bot number
def bot_compare(user_number):
    bot_choice = random.randint(10, 21)

    if (user_number > bot_choice):
        print("The bot's result was only", bot_choice, "You win!")
                        
    elif (user_number < bot_choice):
        print("The bot's result was", bot_choice, "You lose!")
                        
    elif (user_number == bot_choice):
        print("The bot's result was also", bot_choice, "It's a tie!")
        
    else:
        print("error getting results")      

#main guess a number function
def guess_a_number():
    time.sleep(0.8)
    print("You will have to guess a random number from 1 - 100, goodluck!")

    number_answer = random.randint(1, 100)

    while True:
        try:
            users_guess = int(input("Your guess: "))
            if (users_guess == number_answer):
                print("You got it! You win!")
                break
            elif (users_guess > number_answer):
                print("Your guess is too high! Try again!")
                pass
            elif (users_guess < number_answer):
                print("Your guess is too low! Try again!")
                pass
            else:
                print("error")
                break
        except ValueError:
            print("Please enter a valid guess")
            pass

#calling main function
if __name__ == "__main__":
    main()