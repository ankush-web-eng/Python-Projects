const = ["start", "continue", "stop", "pause"]
import random
random_var = random.choice(const)
print(f"Your random variable is {random_var}")
pyaar  = len(random_var)
display = []
for spaces in range(pyaar):
    display += "_"

isEnded = False
lives = 6
while not isEnded:
    print(f"You have {lives} lives!")
    guess = input("Enter a letter:")
    
    for position in range(pyaar):
        letter = random_var[position]
        if(letter ==  guess):
            display[position] = guess
    if guess not in random_var:
        lives -= 1
        if lives == 0:
            isEnded = True
            print("You lost the game!")
    
    print(f"{' '.join(display)}")
    if "_" not in display:
        isEnded = True
        print("You won the game!")
 
