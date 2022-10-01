import math
def test(number):
   n=number
   while(n!=1):
    if n == 1:
        print(n)
        break
    if (n % 2) == 0:
        n=n/2
        print(n)
        continue
    else:
        n=(n*3)+1
        
import math

def squaremeter(n):
    squaremeters = []
    rest = n
    while n > 0:
        rest = math.floor(math.sqrt(n))**2
        squaremeters.append(rest)
        n-= rest
    
    return(squaremeters)



def square(n):
    lis = []
    
    rest = n
    while n > 0:
        rest = math.floor(math.sqrt(n))**2
        lis.append(rest)
        n-= rest
    return(lis)

def square_prompt():
    n = 1
    while n>0:
        n = float(input(" Please Enter any numeric Value : "))
        if n:
            print(square(n))

# square_prompt()

import math

def squaremeter(number):
    givenNumber=number
    squareleft = givenNumber
    squaremeters = []
   
    while givenNumber > 0:
        squareleft = math.floor(math.sqrt(givenNumber))**2
        squaremeters.append(squareleft)
        givenNumber=givenNumber- squareleft
    return(squaremeters)

# print(func(22))
# print(func(15324))

# # test(42)
# print(squaremeter(12))
print(squaremeter(12))