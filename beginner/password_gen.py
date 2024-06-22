import random
num = int(input("Enter the length of your Password:"))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
char = input("Do you want special characters? yes or no (Case Sensitive)")
if (char == "yes"):
    characters += "!@#$%&?"
numbers = input("Do you want numbers? yes or no (Case Sensitive)")
if(numbers == "yes"):
    characters += "123456789"
Password = ""
for i in range(1,num+1):
    random_char = random.choice(characters)
    Password += random_char
print(f"Your Password is : {Password}")