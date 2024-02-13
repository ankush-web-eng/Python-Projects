import random
def random_card():
    cards = ['11','2','3','4','5','7','6','8','9','10','10','10',]
    card = random.choice(cards)
    return int(card)

def cards_sum(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(card1, card2):
    a = card1
    b = card2
    if a == b:
        print("It's a Draw!!")
    elif a == 0:
        print(f"You Won, You have a BlackJack!! Your score is {a} and computer's score is {b}")
    elif b == 0:
        print(f"You Lost, oponent has a BlackJack!! Your score is {a} and computer's score is {b}")
    elif a>21:
        print(f"You Lost, you exceeded{a}!! Your score is {a} and computer's score is {b}")
    elif b <21:
        print(f"You Won, YOur Oppenent exceeded: {b}!! Your score is {a} and computer's score is {b}")
    elif a>b:
        print(f"You Won by higher Score: {a}!! Your score is {a} and computer's score is {b}")
    elif b>a:
        print(f"You Lost, Oponent has higher Score: {b}!! Your score is {a} and computer's score is {b}")

user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(random_card())
    computer_cards.append(random_card())

isEnded = False
while not isEnded:
    user_score = int(cards_sum(user_cards))
    computer_score = int(cards_sum(computer_cards))

    print(f"Your Score is {user_score} and Cards are {user_cards}")
    print(f"Computer Cards are {computer_cards[0]}")

    if user_score == 0 or computer_score ==0 or user_score > 21:
        isEnded = True
    else:
        user_should_play = input("Do you want to play more? 'y' or 'n':")
        if user_should_play == 'y':
            user_cards.append(random_card())
        else:
            isEnded = True

while computer_score !=0 and computer_score<17:
    computer_cards.append(random_card())
    computer_score = sum(computer_cards)


compare(user_score,computer_score)