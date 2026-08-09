
#Welcome Message

print("Welcome to the Number Guessing Game!\nI'm thinking of a number from 1 to 10.".upper())

#importing required module

import random 

print("Enter The Difficulty:\n1.Easy(5 chances)\n2.Medium(3 chances)\n3.Hard(1 chance)\n4.Exit\n")
# User choosing a difficulty

while True:
    try:
        choice=int(input("Select the difficulty (1)(2)(3) or (4) to exit:"))
        if choice in [1,2,3,4]:

            attempts=1

            if choice==1:

                print(f"Your Choice is: {choice}.Easy")
                print("\t\tYou have 5 Chances")
                chances=5
                
                comp_guess=random.randint(1,10)

                for chance in range(5):
                    
                    user_guess=int(input("Enter a number from (1) to (10):"))

                    if user_guess!=comp_guess:
                   
                        chances-=1
                        attempts+=1
                        print(f"Wrong guess!\nChances Left:{chances}")

                        if chances==0:

                            print(f"You lose chances left {chances}. Retry")
                            print(f"The computer had guessed {comp_guess}")
                            break

                    else:

                        print(f"You win in {attempts} attempt(s)\n computer had guessed {comp_guess}")
                        break
                
            elif choice==2:

                print(f"Your Choice is: {choice}.Medium")  
                print("\t\tYou have 3 Chances") 
                chances=3
                
                comp_guess=random.randint(1,10)

                for chance in range(3):
                    
                    user_guess=int(input("Enter a number from (1) to (10):"))

                    if user_guess!=comp_guess:

                        chances-=1
                        attempts+=1
                        print(f"Wrong guess!\nChances Left:{chances}")

                        if chances==0:

                            print(f"You lose chances left {chances}. Retry")
                            print(f"The computer had guessed {comp_guess}")
                            break

                    else:

                        print(f"You win in {attempts} attempt(s)\n computer had guessed {comp_guess}") 
                        break

            elif choice==3:

                print(f"Your Choice is: {choice}.Hard")
                print("\t\tYou have 1 chance only!")
                chances=1
                
                comp_guess=random.randint(1,10)

                for chance in range(1):

                    user_guess=int(input("Enter a number from (1) to (10):"))

                    if user_guess!=comp_guess:

                        chances-=1
                        attempts+=1
                        print(f"Wrong guess!\nChances Left:{chances}")

                        if chances==0:

                            print(f"You lose chances left {chances}. Retry")
                            print(f"The computer had guessed {comp_guess}")
                            break

                    else:

                        print(f"You win\ncomputer had guessed {comp_guess}") 
                        break

            else:

                print("Exiting...")
                break

        else:

            print("Select difficulty in 1,2 or 3")

    except ValueError:
        print("INVALID INPUT!\nEnter 1,2,3 or 4 only")   



