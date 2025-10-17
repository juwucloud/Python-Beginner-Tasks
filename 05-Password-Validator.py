

#Get User Input
PasswordCheck = input("What is your new password?: ")
lengthcounter = 0
stringchecker = False
numberchecker = False

for index in PasswordCheck:
    if index.isalpha() == True:
        stringchecker == True
        print (stringchecker)
    else:
        print ("no string")