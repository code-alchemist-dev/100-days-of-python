print('Leap Year Challenge!!!\n')

# Prompt the user to enter a year and convert it to an integer
year = int(input('Please enter your desired year: '))

# Print instructions for the pizza order
print('Pizza Order Instructions!!!')

# Initialize the total bill to 0.0
total_bill = 0.0

# Prompt the user to choose the size of the pizza
pizza_size = input('''
                   Please choose the size of the pizza you prefer\n' 
                    S, M, or L\n\n
                   ''')

# Determine the price based on the pizza size
if pizza_size.lower() == 's':
    # Small pizza costs 30
    total_bill += 30
    print(f'Current bill: R{total_bill}\n')
elif pizza_size == 'M':
    # Medium pizza costs 60
    total_bill += 60
    print(f'Current bill: R{total_bill}\n')
elif pizza_size == 'L':
    # Large pizza costs 90
    total_bill += 90
    print(f'Current bill: R{total_bill}\n')
else:
    # Handle invalid pizza size input
    print('Invalid pizza size dummy!!!')
    quit()

# Prompt the user to add pepperoni
add_pepperoni = input('''
                  Would you like to add Pepperoni?\n
                  Y or N \n\n
                  ''')

# Determine the price if pepperoni is added
if add_pepperoni.lower() == 'y':
    # Adding pepperoni costs 15
    total_bill += 15
    print(f'Current bill: R{total_bill}\n')
elif add_pepperoni == 'N':
    # No additional cost if pepperoni is not added
    print(f'Current bill: R{total_bill}\n')
else:
    # Handle invalid input for pepperoni addition
    print(f'Current bill: R{total_bill}')
    quit()

# Prompt the user to add extra cheese
add_extra_cheese = input('''
                         Would you like to add extra cheese?\n
                         Y or N \n\n
                         ''')

# Determine the price if extra cheese is added
if add_extra_cheese.lower() == 'y':
    # Adding extra cheese costs 12
    total_bill += 12

# Print the total bill for the pizza
print(f'Total bill: R{total_bill} for your Pizza, Enjoy!!!')
