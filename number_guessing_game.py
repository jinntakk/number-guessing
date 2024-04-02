import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 #set up variable that isn't between 1 and x
    while guess != random_number:
        guess = int(input(f"pick a number between 1 and {x} "))
        if guess < random_number:
            print("Sorry too low")
        elif guess > random_number:
            print("Too high!")

    print(f"Correct number! {random_number}")

guess(1000) #pick random number
