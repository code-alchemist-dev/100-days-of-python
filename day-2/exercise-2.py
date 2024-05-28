print('BMI Calculator! \n')

# Prompt the user to enter their weight in kilograms and height in meters
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))

print('\n')

# Calculate the BMI and round it to one decimal place
bmi = str(round(weight / height ** 2, 1))

# Display the calculated BMI
print('Your BMI is: ' + bmi)
