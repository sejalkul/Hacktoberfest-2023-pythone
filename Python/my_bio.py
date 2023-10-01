# Get the user's name as input and handle empty input
name = input("Enter your name: ").strip()

# Validate name input
while not name:
    print("Name cannot be empty.")
    name = input("Enter your name: ").strip()

# Get the user's birth year as input and handle invalid input
while True:
    try:
        birth_year = int(input("Enter your birth year: "))
        break  # Exit the loop if the input is a valid integer
    except ValueError:
        print("Invalid input. Please enter a valid year.")

# Calculate the user's age
current_year = 2023  # You can change this to the current year
age = current_year - birth_year

# Print the greeting with the user's name and age
print(f"Hello {name}, your age is {age} years old.")

