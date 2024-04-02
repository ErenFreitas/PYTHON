# Define the person's data
name = 'Eren Freitas'
height = 1.70
weight = 60 

# Calculate BMI
bmi = weight / (height * height) 

# Print the data without using f-strings
print(name, 'is', height, 'meters tall.')
print('He weighs', weight, 'kilograms and his BMI is', bmi)

# Introducing f-strings

# Print the data using f-strings
print(f"{name} is {height} meters tall.")
# The next line prints weight, rounding BMI to 2 decimal places
print(f"Weighs {weight} kilograms and their BMI is {bmi:.2f}.")
