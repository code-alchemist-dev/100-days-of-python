print('Odd or Even!!!\n')

# Prompt the user to enter a whole number and convert the input to an integer
number = int(input('Please enter a whole number: '))

# Check if the number is divisible by 2
if number % 2 == 0:
    # If the remainder is 0, the number is even
    print(f'{number} is an Even number')
else:
    # If the remainder is not 0, the number is odd
    print(f'{number} is an odd number')

    