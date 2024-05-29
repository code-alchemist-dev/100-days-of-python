print('Leap Year Challenge!!!\n')

# Prompt the user to enter a year and convert the input to an integer
year = int(input('Please enter your desired year: '))

# Check if the year is divisible by 4
if year % 4 == 0:
    # Further check if the year is also divisible by 100
    if year % 100 == 0:
        # Check if the year is divisible by 400 to determine if it's a leap year
        if year % 400 == 0:
            print(f'{year} is a leap year.')
        else:
            # If the year is divisible by 100 but not by 400, it is not a leap year
            print(f'{year} is not a leap year.')
    else:
        # If the year is divisible by 4 but not by 100, it is a leap year
        print(f'{year} is a leap year.')
else:
    # If the year is not divisible by 4, it is not a leap year
    print(f'{year} is not a leap year.')
