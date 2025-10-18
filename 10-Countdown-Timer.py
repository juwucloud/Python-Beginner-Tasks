import time

sec = int(input("How long do you want to wait? (seconds) \n\n"))
print("")
print("")


                
for i in range(sec, -1, -1):
    print (i)
    time.sleep(1)
print ("Time's up!")

