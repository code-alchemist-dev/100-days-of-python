print('Remaining Life Calculator! \n')

# Prompt the user to enter a person's age
age = int(input('Enter age: '))

# Calculating remainging years, days, month and weeks
remaining_years = 90 - age
remaining_days = remaining_years * 365
remaining_weeks = remaining_years * 52
remaining_months = remaining_years * 12

print('\n')

print(f'You {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left to live.')