word = input ("Is your word a palindrome? Type your word\n")

def palicheck(a):
    rev = a[::-1]
    for letter in range(len(a)):
        if a == rev:
            comparison = True
        else:
            comparison = False
    return comparison
    
        
if palicheck(word) == True:
    print (f"The word {word} is a palindrome!")
else:
    print (f"The word {word} is NOT a palindrome!")