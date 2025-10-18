print("Welcome to the Interest Calculator!")
print("Tell us your Principal, Rate and the Time for your Interest")


while True:
    try:
        principal = float(input("Principal (€): ")).replace(",", "."))
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        rate = float(input("Rate: ")).replace(",", "."))
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        time = int(input("Time (in years): ")).replace(",", "."))
        break
    except ValueError:
        print("Please enter a valid number")


interest = (principal * rate * time) / 100

print(f"\nYour interest after {time} years is {interest:.2f} €")
total = principal + interest
print(f"Total amount after {time} years: {total:.2f} €")




