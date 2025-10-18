# User Input

CheckNumber = int(input("What number you want to check for primes?"))

def primecheck(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
        else:
            return True
    

if primecheck(CheckNumber) == True:
    print (f"The Number {CheckNumber} is a Prime")
else:
    print (f"The Number {CheckNumber} is NOT a Prime")
            
