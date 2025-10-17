

#Get User Input
PasswordCheck = input("What is your new password?: ")

passedCheck = False


# checks if String is in the Password
def isString(a):
    stringchecker = False
    for index in a:
        if index.isalpha() == True:
            stringchecker = True
    print(f"Password contains a String: {stringchecker}")

# checks if Number is in the Password
def isNumber(a):
    numberchecker = False
    for index in a:
        if index.isnumeric() == True:
            numberchecker = True
    print(f"Password contains a Number: {numberchecker}")


# checks password length
def isLongEnough(a):
    lengthcounter = 0
    for index in a:
        lengthcounter += 1
    if lengthcounter >= 8:
        return True
    else:
        return False


        

# numberchecker = False



#isString(PasswordCheck)



