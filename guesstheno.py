import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
numbers = range(1,101)
num_choice = random.choice(numbers)
def game(lives):
    while lives > 0:
        guess = int(input("guess:\n"))
        if guess == num_choice:
            print("you got it!")
            return
        elif guess != num_choice:
            lives -= 1
            if guess > num_choice:
                print("too high")
            elif guess < num_choice:
                print("too low")
            print(f"you have{lives} lives left..")
    if lives == 0:
        print(f"game over.. you lose. number was {num_choice}")




choose =input("Choose a difficulty. Type 'easy' or 'hard':\n ").lower()
if choose == "easy":
    print("you have 10 lives.start guessing..")
    lives =10
    game(lives)


if choose == "hard":
    print("you have 5 lives.start guessing..")
    lives= 5
    game(lives)

