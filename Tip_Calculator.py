print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
split = int(input("How many people to split the bill?\nPeople:"))

total = (((bill * (tip / 100)) + bill) / split)
total_rounded = round(total, 2)
print(f"Each person should pay: ${total_rounded}")
