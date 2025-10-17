
# checks if String is in the Password
def isString(a):
    stringchecker = False
    for index in a:
        if index.isalpha() == True:
            stringchecker = True
    return stringchecker

# checks if Number is in the Password
def isNumber(a):
    numberchecker = False
    for index in a:
        if index.isnumeric() == True:
            numberchecker = True
    return numberchecker


# checks password length
def isLongEnough(a):
    lengthcounter = 0
    for index in a:
        lengthcounter += 1
    if lengthcounter >= 8:
        return True
    else:
        return False

# Main check
def passwordchecker():
    PasswordCheck = input("What is your new password?: ")
    if isString(PasswordCheck) == True and isNumber(PasswordCheck) == True and isLongEnough(PasswordCheck) == True:
        print ("Your Password meets all criteria!")
    else:
        print ("Your Password is insufficient")


passwordchecker()

