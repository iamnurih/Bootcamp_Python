import random
#the code asks the omputer to bring a module to play the random game

print("Welcome to the <Guess the number> game")
print("The machine will pick a number from between 1-100")
print("Guess the number!")
# This is a three-line introduction. It explains the game. 

randomly_picked_number = random.randint(1,100)
attempts = 0
"""this is a pre-set function, 
it asks the machine to return a random number between the number in () 
in this case, the range is 1 to 100. 
It works because random module is imported in the beginning. 
""" 

while True: 
    guess = int(input("숫자를 입력하세요 (1-100): "))
    attempts += 1

    if guess == randomly_picked_number:
        print(f"Congratulations! You've called the right number {randomly_picked_number}!")
        print(f"You got the number right in {attempts} atempts")
        break

    elif guess < randomly_picked_number: 
        print(f"Pick a larger number than {guess}!")

    else: 
        print(f"Pick a smaller number than {guess}!")

print("This is the end of the game. \nTry again next time")



# It didn't work at the first attempt. 
# The problem was indention. I forgot to indent If, elif, else (and the print underneath)
# I forgot to add break at the end of "if," so it endlessly played the game. 
