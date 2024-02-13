from random import randint
print("Welcome to the Number Guessing Game!!")
print("Well, I am thinking of a number between 1 and 100")
level = input("Choose the difficulty level. Type 'easy' or 'hard': ")
if level == 'easy':
    print("You have 10 attempts!")
else:
    print("You have 5 attempts!")

random_num = randint(1,100)

lives = 10 if level == 'easy' else 5

isEnded = True
while isEnded:
    num = int(input("Make a guess: "))
    if random_num == num:
        print("Congratulations, you made a right guess!!")
        isEnded = False
    elif num > random_num:
        print("Too High!")
        lives -=1
        print(f"You have {lives} left!")
    else:
        print("Too Low!")
        lives -=1
        print(f"You have {lives} left!")
    if lives == 0:
        isEnded = False
        print("You ran out of lives!!")
