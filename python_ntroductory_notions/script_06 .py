import random as number_guess
number_random_system = number_guess.randint(0, 10)
numerber_user = 0
attempet = 0

while numerber_user != number_random_system:

    print("Enter the number !")
    numerber_user = int(input())
    
    if numerber_user == number_random_system:
        print(f"number choose {numerber_user}, congratulations you're right!")
    else:
        print(f"number choose: {number_random_system}, sorry try again")
    
    attempet += 1
    print(f"Number attempet {attempet}")


