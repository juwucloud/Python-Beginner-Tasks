

#Get User Input
PasswordCheck = input("What is your new password?: ")



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




# lengthcounter = 0
# numberchecker = False



#isString(PasswordCheck)



