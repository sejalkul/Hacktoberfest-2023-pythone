# Get the user's name as input
name = input("Enter your name: ")

# Get the user's birth year as input and convert it to an integer
birth_year = int(input("Enter your birth year: "))

# Calculate the user's age
current_year = 2023  # You can change this to the current year
age = current_year - birth_year

# Print the greeting with the user's name and age
print(f"Hello {name}, your age is {age} years old.")
