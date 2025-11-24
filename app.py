print("Welcome to my Python program!")

#Asks for input
hours = input("How many hours did you study today? ")
hours = float(hours)
weekly_hours = hours * 7

#Prints the input * seven
print(f"You are on track to study {weekly_hours} hours this week.")

#Attempts to convert the integer into a string, if impossible then provides another input for a valid number.
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
