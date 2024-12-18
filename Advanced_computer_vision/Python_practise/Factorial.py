#Factorial of a number using python while loop

def Facto(a):
    fact=1
    while a>0:
        fact=fact*a
        a-=1
    print(fact)

Facto(0)

# USing recursion

def Fact(a ,b):
    if b=="R":
        if a==0:
            return 1
        else:
            return a*Fact(a-1,"R")
    else:
        Facto(a)
        
print(Fact(5,"M"))
    