def Addition(num1, num2):
    return num1+num2

def Subtraction(num1,num2):
    return num1-num2

def Multiplication(num1,num2):
    return num1*num2

def Division(num1,num2):
    return num1/num2

operation = {
    "+" : Addition,
    "-": Subtraction,
    "*": Multiplication,
    "/": Division
}
def Calculator():
    isContinue = True
    num1 = int(input("Enter your first Number:"))
    for o in operation:
        print(o)
    while isContinue:
        desired_operation = input("Enter your desired opeartion:")
        num2 = int(input("Enter Second Number:"))
        done_operation = operation[desired_operation]
        answer = done_operation(num1,num2)

        print(f"{num1} {desired_operation} {num2} = {answer}")
        ques = input(f"Do you want to carry out more calculation with {answer}? 'y' for yes, 'n' for no and 'r' for fresh calculation:")
        if ques == 'y':
            num1 = answer
        if ques == 'n':
            isContinue = False
        else:
            Calculator()
        
Calculator()