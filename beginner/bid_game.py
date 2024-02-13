const = {}
notFinished = True
while notFinished:
    name = input("What is your name?:")
    bid = int(input("What is your bid?$"))
    const[name] = bid
    many = input("Is there any other person to bid? 'y' or 'n'")
    if many == 'n':
        notFinished = False

for i in const:
    price = 0
    if const[i] > price:
        price = const[i]
        person = i
print(f"Hishest bid is of {price} by {person}")