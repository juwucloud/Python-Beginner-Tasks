import time


while True:
    try:
        sec = int(input("How long do you want to wait? (seconds) "))
        break
    except ValueError:
        print("Please enter a valid number")
        
print("")

                
for i in range(sec, 0, -1):
    print (i)
    time.sleep(1)
print ("Time's up!")

