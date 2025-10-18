def palicheck(a):
    rev = a[::-1]
    for letter in range(len(a)):
        if a[letter] != rev[letter]:
            return False
    return True

# Main
def main():
    word = input ("Is your word a palindrome? Type your word\n")
    if palicheck(word.lower()) == True:
        print (f"The word {word} is a palindrome!")
    else:
        print (f"The word {word} is NOT a palindrome!")


main()

while True:
    again = input ("Test another word? (y/n) ".lower())
    if again == "y" or again =="yes":
        main()
    elif again == "n" or again == "no":
        print ("Thank you for using PalindromeChecker")
        break
    else:
        print ("Invalid Character, please type y or n")