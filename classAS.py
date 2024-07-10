#   < ==============================================Week 2======================================================== >

<=============Q.1==============>
n = int(input("Enter Number"))
if n%7 ==0:
    print("True")
else:
    print("False")

#<=============Q.2==============>

n = int(input("Enter the number:"))

def lastDigit(num):
    if num % 10 == 4:
        return 1
    else:
        return 0

star = lastDigit(n)
if star == 1:
    print("It's last digit is 4!")
else:
    print("Last digit is not 4!!")

#<=============Q.3==============>

n = input("Enter a number:")
n = int(n)
if (n%10==4 and n%3==0):
    print("Successful")
else:
    print("False")

# <=============Q.4==============>

n = input("Enter a number:")
n = int(n)
if (n%10==5 or n%7==0):
    print("Successful")
else:
    print("False")

# <=============Q.5==============>

n = input("Enter a number:")
n = int(n)
if (n%5==0 and n%11==0):
    print("Successful")
else:
    print("False")

# <=============Q.6==============>

a = int(input("Enter Number:"))
b = int(input("Enter Number:"))
c = int(input("Enter Number:"))
max = 0
max = a if a>b else  b
if max<c:
    max = c 
print(f"Max is {max}")


# <=============Q.7==============>

a = int(input('Enter side os triangle'))
b = int(input('Enter side os triangle'))
c = int(input('Enter side os triangle'))
if a+b+c == 180:

    if a==90 or b==90 or c==90:
        print("Triangle is 'Right Angle'")
    elif a>90 or b>90 or c>90:
        print("Triangle is 'Obtuse'")
    else:
        print("Triangle is 'Acute'")
else:
    print("Enter valid angles")

# <=============Q.8==============>

n = int(input("Enter your age:"))
if(n>=18):
    print("Eligible!")
else:
    print("Not Eligible")

# <=============Q.9==============>

year = int(input("Enter the year:"))
if year %4 == 0:
    if year % 100 !=0:
        print("Leap Year!!")
    else:
        if year%400 ==0:
            print("Leap Year!!")
        else:
            print("Not a Leap Year!!")
else:
    print("Not a Leap Year!!")
# <=============Q.11==============>

a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
d = int(input("Enter a number:"))
e = int(input("Enter a number:"))
avr = ((a+b+c+d+e)/5)
print(f"Average is {avr}")


# <=============Q.12==============>
    
a = int(input('Enter side os triangle'))
b = int(input('Enter side os triangle'))
c = int(input('Enter side os triangle'))
if a+b+c == 180:
    print("Valid")
else:
    print("invalid!")

# <=============Q.13==============>

a = int(input("Enter number:"))
b = int(input("Enter number:"))
max = 0
max=a if a>b else  b
print(f"Max is {max}")

# <=============Q.14==============>

a = int(input("Enter Number:"))
b = int(input("Enter Number:"))
c = int(input("Enter Number:"))
min = 0
min = a if a<b else b
min = c if min>c else min
print(f"Min is {min}")




#  <===============================================Week 3=========================================================>

#<==============Q.1==============>

n = int(input("Enter a number:"))
for i in range(1,n+1):
    print(i, sep="_")


#<==============Q.2==============>

n = int(input("Enter a number:"))
for i in range(n,0,-1):
    print(i, sep="_")

#<==============Q.3==============>

n = int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)

#<==============Q.4==============>

n = int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2!=0:
        print(i)

#<==============Q.5==============>

n = int(input("Enter a NUmber:"))
sum = 0
for i in range(1, n+1):
    sum += i
print(f"Total sum is {sum}")

#<==============Q.6==============>

n = int(input("Enter a number:"))
sum = 0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(f"Sum of all even numbers is {sum}")

#<==============Q.7==============>

n = int(input("Enter a number:"))
sum = 0
for i in range(1,n+1):
    if i%2!=0:
        sum+=i
print(f"Sum of all odd numbers is {sum}")


#<==============Q.8==============>

# n = input("Enter the Number:")
# print(len(n))
n = int(input("Enter the Number:"))
c = 0
while n>1:
    rem = n/10
    c+=1
    n = rem
print(f"Total digits in Number are: {c}")

#<==============Q.9==============>

n = int(input("Enter a Number:"))
sum = 0
while n>1:
    rem = int(n%10)
    sum += rem
    loop = n/10
    n = loop
print(f"Sum of digits is {sum}")

#<==============Q.11==============>

a = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")

#<==============Q.12==============>

a = int(input("Enter base: "))
b = int(input("Enter power: "))

print(f"Answer is {a**b}")


# <====================================Week 4==================================================================>

#<=============Q.1=================>

a = int(input("Enter a number:"))
for i in range(1,a+1):
    print("*"*a)


#<=============Q.2=================>
    
a = int(input("Enter a number:"))
for i in range(1,a+1):
    print("*"*i)

#<=============Q.3=================>
    
a = int(input("Enter a number:"))
for i in range(1,a+1):
    print("*"*((a+1)-i))

#<=============Q.4=================>

a = int(input("Enter height: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        if j%2==0:
            print("*",end="")
        else:
            print(j, end="")
    print()

#<=============Q.5=================>

a = int(input("Enter height: "))
b = int(input("Enter width: "))
for i in range(1,a+1):
    print("*" + "_"*(b-2) + "*")

#<=============Q.6=================>

a = int(input("Enter height: "))
b = int(input("Enter width: "))
for i in range(1,a+1):
    print("*" + "_"* (b-i-1) + "*")

#<=============Q.7=================>
    
a = int(input("Enter height: "))
for i in range(1,a+1):
    print("_"*(a-i)+ "*"*i)

#<=============Q.8=================>

a = int(input("Enter height: "))

for i in range(a):
    print("_"*i + "*"*(a-i))

#<=============Q.9=================>

a = int(input("Enter height:"))

for i in range(a):
    print("*"*(a-i) + " " * i +" " * i + "*"*(a-i))

#<=============Q.10=================>
    
a = int(input("Enter height:"))

for i in range(1,a+1):
    print("*"*i + " " * (a-i) + " " * (a-i) + "*"*i)

#<=============Q.11=================>

a = int(input("Enter height: "))

for i in range(a):
    print("*"*(a-i) + " " * i +" " * i + "*"*(a-i))
for i in range(1,a+1):
    print("*"*i + " " * (a-i) + " " * (a-i) + "*"*i)

#<=============Q.12=================>

for i in range(1,10):
    for j in range(1,i+1):
        print(j,end="")
    print()

#<=============Q.13=================>

for i in range(5,0, -1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#<=============Q.14=================>

k=1
for i in range(1,5):
    for j in range(i):
        print(k,end="")
        k +=1
    print()

#<=============Q.15=================>

a = int(input("Enter height: "))
for i in range(1,a+1):
    print("*"*i)
for i in range(1,a+1):
    print("*"*(a-i))

#< ==== Practice==== >

a = int(input("Enter height:"))
for i in range(1,a+1):
    for j in range(a,i,-1):
        print(" ", end="")
    for k in range(i,1,-1):
        print(k,end="")
    for l in range(1,i+1):
        print(l,end="")
    print()

for i in range(a,0,-1):
    for j in range(a-i+1):
        print(" ",end="") 
    for k in range(1,i-1):
        print((i-k),end="")
    for l in range(1,i):
        print(l,end="")
    print()

#< ==== Practice==== >

a = int(input("Enter height:"))
for i in range(1,1+a):
    for j in range(a,i,-1):
        print(" ", end="")
    print("*",end="")
    for j in range(1,i):
        print(" ", end="")
        print(" ", end="")
    print("*", end="")
    print()
for i in range(a,0,-1):
    for j in range(a-i+1):
        print(" ", end="")
    print("*", end="")
    for k in range(1,i):
        print(" ", end="")
        print(" ", end="")
    print("*", end="")
    print()
for i in range(a,0,-1):
    for j in range(a-i+1):
        print(" ",end="") 
    for k in range(1,i):
        print(" ",end="")
    print("*", end="")
    for l in range(1,i):
        print(l,end="")
    print()

# <====================================Week 5==================================================================>

#<=============Q.1=================>

A = [1,2,3,4,5]
sum = 0
for a in A:
    sum  += a
print(f"Sum is {sum}")

#<=============Q.2=================>

A = [1,2,3,4,5]
B = []
b = int(input("Scaler: "))
for a in A:
    a += b
    B.append(a)
print(B)

n = int(input("Enter number of elements in your array: "))
l = list()
for a in range(n):
    p = int(input("Enter Element:"))
    l.append(p)
print(l)

#<=============Q.3=================>

n = int(input("Enter number of elements in your array: "))
A = list()
for a in range(n):
    p = int(input("Enter Element:"))
    A.append(p)
max = 0
for i in A:
    if max<i:
        max = i
print(f"MAx is {max}")

#<=============Q.4=================>

n = int(input("Enter number of elements in your array: "))
A = list()
for a in range(n):
    p = int(input("Enter Element:"))
    A.append(p)
s = int(input("Enter Element to be searched:"))
for k in A:
    if k == s:
        print(f"Element is present!!")
    
#<=============Q.5=================>

n = int(input("Enter number of elements in your array: "))
A = list()
B = list()
for a in range(n):
    p = int(input("Enter Element:"))
    A.append(p)
for i in A:
    if i < 0:
        B.append(i)
print(B)

#<=============Q.6================>

n = int(input("Enter number of elements in your array: "))
A = list()
for a in range(n):
    p = int(input("Enter Element:"))
    A.append(p)
even = 0
odd = 0
for i in A:
    if i%2==0:
        even += 1
    else:
        odd +=1
print(f"Absolute Diffesrence is {abs(even-odd)}")

#<=============Q.7=================>

n = int(input("Enter number of elements in your array: "))
A = list()
E = list()
O = list()
for a in range(n):
    p = int(input("Enter Element:"))
    A.append(p)
for i in A:
    if i %2==0:
        E.append(i)
    else:
        O.append(i)
print(f"Even elements are {E}")
print(f"Odd elements are {O}")

#<=============Q.8=================>

n = int(input("Enter number of elements in your array: "))
A = list()
S = list()
for a in range(n):
    p = int(input("Enter Element:"))
    A.append(p)
for i in A:
    p = i*i
    S.append(p)
print(S)

# <=============Q.9=================>

n = int(input("Enter number of elements in your array: "))
A = list()
S = list()
for a in range(n):
    p = int(input("Enter Element:"))
    A.append(p)
for i in A:
    p = i*i*i
    S.append(p)
print(S)

# <=============Q.9=================>

n = int(input("Enter number of elements in your array: "))
A = list()
R = list()
for a in range(n):
    p = int(input("Enter Element:"))
    A.append(p)
A.reverse()

# <====================================Week 5==================================================================>


# <=============Q.1=================>

a =  int(input("Enter number of elements: "))
li = []

for i in range(a):
    li.append(input("Enter String: "))

for i in li:
    vo = 0
    for j in i:
        if j in "aeiouAEIOU":
            vo += 1

    print(f"Number of vowels in {i} are: {vo}")


# <=============Q.2=================>

st = input("Enter a String: ")
print(len(st))

# <=============Q.3=================>

n = int(input("Enter length of String: "))
li = []

for i in range(n):
    li.append(input("Enter your String: "))
for j in li:
    print(int(j==j[::-1]))

# <=============Q.4=================>

st = input("Enter a String: ")
for i in range(len(st)):
    if st[i] != "*":
        pr = st[i::]
        break
st = pr
pt = st[::-1]
for i in range(len(pt)):
    if pt[i] != "*":
        kt = pt[i::]
        break
st = kt[::-1]
print(st)

# <=============Q.5=================>

n = int(input("Enter number of String: "))
li = []
ki = []
for i in range(n):
    li.append(input("Enter you Word: "))

for i in li:
    t = i[::-1]
    ki.append(t)
print(ki)

# <=============Q.6=================>

a = input('Enter a String:')
print(a[::-1])

# <=============Q.7=================>

s = input("Enter a String:")
n = int(input("Enter ASCII code:"))
if chr(n) in s:
    print(s.find(chr(n)))
else:
    print("Doesn't Exist!!")

# <=============Q.8=================>

a = input("Enter first Sting: ")
b = input("Enter second Sting: ")
if b in a:
    print(a.find(b))
else:
    print("!!!!")

# <=============Q.9=================>

string = ["A", "n", "k", "U", "s", "H"]
p = []
for i in string:
    p.append(i.lower())
print(p)

# <=============Q.10=================>

string = ["A", "n", "k", "U", "s", "H"]
p = []
for i in string:
    p.append(i.capitalize())
print(p)

# <===================================Week 7==========================================>

# <==============Q.1===============>

l1 = eval(input("Enter: "))
l2 = eval(input("Enter: "))
l = []
for i in set(l1):
    if i in l2:
        x = min(l1.count(i), l2.count(i))
        y = [i]*x
        l.extend(y)
print(l)

# <==============Q.2===============>

l = eval(input("Enter: "))
for i in l:
    if l.count(i)>1:
        print(i)
        break
else:
    print("-1")

# <==============Q.3===============>

s=input("Enter your String: ")
if len(s)%2==0:
    for i in set(s):
        if s.count(i) %2 != 0:
            print(0)
            break
    else:
        print(1)
else:
    c = 0
    for i in set(s):
        if s.count(i) %2 !=0 and c == 0:
            c +=1
        elif s.count(i)%2!=0:
            print(0)
            break
    else:
        print(1)

# <==============Q.4===============>

l = []    
F = int(input("Enter frequency: "))
N = int(input("Enter no. of trees: "))
for i in range(N):
    l.append(int(input("Enter height: ")))
c = 0
for i in set(l):
    if l.count(i) == F:
        c += i
if c == 0:
    print(-1)
else:
    print(c)

# <==============Q.5===============>

l = []
N = int(input("Enter no. of elements: "))
for i in range(N):
    l.append(int(input("Element: ")))
# s = l[::-1]
m = []
c=0
for i in range(len(l)):
    for j in range(len(l)-1, -1,-1):
        if l[i] == l[j] and i != j:
            # print(i,j)
            s = abs(i-j)
            m.append(s)
            c +=1
m.sort()
# print(m)
if c == 0:
    print(-1)
else:
    print(m[0])
    # print(c)

# <==============================Practice====================================>

def wrap(string, max_width):
    j = 0
    p = ''
    while j < len(string):
        p += string[j:max_width+j]
        j += max_width
        print(p)
        p = ''
wrap('ankushankushankush', 6)


n = int(input("Enter no.: "))
li = []
for i in range(2,n+1):
    flag = True
    for j in range(2,(i//2)+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        li.append(i)
print(li)
l2 = []
for i in range(len(li)):
    for j in range(len(li)):
        if li[i] + li[j] == n:
            l2.append([li[i], li[j]])
print(l2)

from random import randint

names = ["Ankush", "Abhay", "Harshit", "Abhishek", "Anant"]
scores = {student:randint(1,100) for student in names}
print(scores)
passed = {student:score for (student, score) in scores.items() if score > 48}
print(passed)

p = [1,2,3,2,1,2,3]
s = p
# print(s)
freq = {}
for i in s:
    freq[i] = s.count(i)
    while i in s:
        s.remove(i)
print(freq)

a = "Ankush Deshwal"
b = a.split()

li = []

for i in range(len(min(b))):
    li.append(b[0][i])
    li.append(b[1][i])
    min = i
s = "".join(li)
p = max(b)
p = p[min+1:len(p)]
s += p
print(s)


# <==================================Week 7 Updated ========================================>

# <================Q.1================>

li = []
for i in range(int(input("Enter number of elements: "))):
    s = int(input("Element: "))
    li.append(s)
p = int(input("Enter the element to be searched: "))
# c = 0
for i in li:
    if i==p:
        c = li.count(i)
print(f"Frequency of {p} is {c}")

# <================Q.2================>

li = []
for i in range(int(input("Enter number of elements: "))):
    s = int(input("Enter: "))
    li.append(s)
p = []
for i in li:
    p.append(li.count(i))
for i in li:
    if li.count(i) == min(p):
        print(f"The least common element is {i}")
        break

# <================Q.3================>

s=input("Enter your String: ")
if len(s)%2==0:
    for i in set(s):
        if s.count(i) %2 != 0:
            print(0)
            break
    else:
        print(1)
else:
    c = 0
    for i in set(s):
        if s.count(i) %2 !=0 and c == 0:
            c +=1
        elif s.count(i)%2!=0:
            print(0)
            break
    else:
        print(1)

# <================Q.4================>
   
li = []
for i in range(int(input("Enter number of elements: "))):
    s = int(input("Enter: "))
    li.append(s)
p = []
flag = True
for i in li:
    if li.count(i) > 1:
        print(f"The first repeating element is {i}")
        flag = False
        break
if flag:
    print(-1)

# <================Q.5================>

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict2.update(dict1)
print(dict2)

# <================Q.6================>

dict1 = {'a': 100, 'b': 400, 'c': 300}
n = 100
for (key, value) in dict1.items():
    if n == value:
        print(True)
        break

# <================Q.7================>

person = {"name": "abc", "age": 25}
for (key, value) in person.items():
    print(key)

# <================Q.8================>

person = {"name": "abc", "age": 25}
for (key, value) in person.items():
    print(value)
    
# <================Q.9================>

person = {"name": "abc", "age": 25}
for (key, value) in person.items():
    print(key, value)

# <================Q.10================>

person = {"name": "abc", "age": 25}
for i in range(len(person)):
    person.popitem()
print(person)

# <================Q.11================>

person = {"name": "abc", "age": 25}
li = []
for (key, value) in person.items():
    li.append(key)
print(li)

# <================Q.12================>

person = {"name": "abc", "age": 25}
li = []
for (key, value) in person.items():
    li.append(value)
print(li)

# <================Q.13================>

li = {}
for i in range(1,int(input("Enter Range: "))+1):
    li[i] = i*i
print(li)

# <================Q.14================>

dict1 = { 1: 'a', 2: 'b', 3: 'c' }
t = []
for (key, value) in dict1.items():
    t.append((key,value))
print(t)

# <================Q.15================>

dict1 = {2: 'Apple', 1:'Mango', 3:'Orange', 4:'Banana'}
a = []
for i in dict1:
    a.append(i)
a.sort()
for i in a:
    print(i,dict1[i])

# <================Q.16================>

A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
l = []
for i in A:
    if i in B:
        l.append(i)
        B.remove(i)
print(l)

# <================Q.17================>

print([i*i for i in range(1,int(input("Enter Range: "))+1)])

# <================Q.18================>

print([i for i in range(1,int(input("Enter Number: "))+1) if i%2==0])

# <================Q.19================>

print([i.upper() for i in input() ])


# <==============================Practice====================================>

from collections import Counter
li = [1,2,3,4,1,2,3,4,5,3,3,5,1,3,8]
p = Counter(li)
d = [i for i in p.items()]
# print(d)
sp = {}
for i in d:
    sp[i[0]] = i[1]
print(sp)

# <==================================Week 8========================================>

import math

# <================Q.1================>

def root(n:int):
    root = str(math.sqrt(n))
    li = root.split(".")
    # print(li)
    if li[1][0]  == '0':
        return int(li[0])
    else:
        return -1
print(root(int(input("Enter Number: "))))

# <================Q.2================>

def square(n:int):
    return n*n
print(square(int(input("Enter Number: "))))

# <================Q.3================>

def area(n:int):
    return 2*math.pi*n
print('{:.2f}'.format(area(int(input("Enter the radius of a circle: ")))))

# <================Q.4================>

def power(a:int, b:int):
    return a**b
print(power(int(input("Enter first Number: ")), int(input("Enter Second number: "))))

# <================Q.5================>

def cube(n:int):
    return n**3
print(cube(int(input("Enter Number: "))))

# <================Q.6================>

def volume(n:int):
    return (4*math.pi*(n**3))/3
print(math.ceil(volume(int(input("Enter Number: ")))))

# <================Q.7================>

def ellipse(a:int, b:int):
    return math.pi*a*b
print('{:.2f}'.format(ellipse(int(input("Enter semi-major axis: ")), int(input("Enter semi-minor axis:")))))

# <================Q.8================>

def slist(n:list):
    return sum(n)
print(slist(map(int,input().split())))

# <====================================Extra Questions==============================>

# <================Q.1================>

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sumof(n):
    return sum(factorial(i) for i in range(1, n+1))

print(sumof(int(input("Enter String: "))))


# <================Q.2================>

def sumof(n):
    su = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            su += i
    return su
print(sumof(int(input('Enter the number : '))))

# <================Q.3================>

def fibo_even(n):
    fib = [0,1]
    su = 0
    for i in range(2,n):
        fib.append(fib[i-2] + fib[i-1])
    print(fib)
    for i in fib:
        if i%2 == 0:
            su+=i
    return su
print(fibo_even(int(input("Enter a Number : "))))

# <================Q.4================>

def fibo_odd(n):
    fib = [0,1]
    su = 0
    for i in range(2,n):
        fib.append(fib[i-2] + fib[i-1])
    print(fib)
    for i in fib:
        if i%2 != 0:
            su+=i
    return su
print(fibo_odd(int(input("Enter a Number : "))))

# <================Q.5================>

def per_square(n:int) -> int:
    p = su =  0
    for i in range(1,n+1):
        su += i**2
        p = i**2
        if p >= n:
            break
    return su
print(per_square(int(input("Enter a Number : "))))

# <================Q.R================>

n = input("Enter String: ")
li = n.split()
ci = []
for i in li:
    ci.append(i[::-1])
print(' '.join(ci))
print(" ".join(li[::-1]))

essay = []
isTrue = True
print("type essay:")
while isTrue:
    n = input()
    if n == "":
        isTrue = False
    else:
        essay.append(n)
p = " ".join(essay)
with open("essay.txt", "w") as file:
    file.write(p)


li = []
for i in range (int(input("Enter number of elements"))):
    p = list(map(int,input("Enter: ").split()))
    li.append(p)
print(li)

n = input("Enter String: ")
if len(n) % 2 == 0:
    for i in n:
        if n.count(i)%2 == 0:
            print(1)
        else:
            print(0)
else:
    c = 0
    for i in n:
        if n.count(i) % 2 != 0 and c == 0:
            c += 1
        elif
