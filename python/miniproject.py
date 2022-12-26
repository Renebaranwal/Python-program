import random
lower =int(input("Enter the lower range:"))
upper =int(input("Enter the upper range:"))
r=random.randint(lower,upper)
print(r)
def eo(r):
    if r%2==0:
        print("number is even")
    else:
        print("number is odd")
eo(r)
def pn(r):
    if r>0:
        print("number is positive")
    elif r<0:
        print("number is negative")
    else:
        print("number is zero")
pn(r)
def pc(r):
    if r<0:
        print("number can neither be composite nor prime because it is negative")
    elif r>1:
        for j in range(2,r):
            if r%j!=0:
                print("number is prime")
                break
            else:
                print("number is composite")
                break
    elif r==1:
        print("number is prime")
pc(r)

