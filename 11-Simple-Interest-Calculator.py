print("Welcome to the Interest Calculator!")
print("Tell us your Principal, Rate and the Time for your Interest")

principal = float(input("Principal (€): "))
rate = float(input("Rate: "))
time = int(input("Time (in years): "))

interest = (principal * rate * time) / 100

print(f"\nYour interest after {time} years is {interest:.2f} €")
total = principal + interest
print(f"Total amount after {time} years: {total:.2f} €")




