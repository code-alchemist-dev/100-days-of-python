# Prompt the user to enter a two-digit number
_input = input('Type a two-digit number: ')

# Separate the input into two characters and convert them to integers
first_digit = int(_input[0])
second_digit = int(_input[1])

# Sum the two digits and convert the result to a string
result = str(first_digit + second_digit)

# Display the result
print('Sum of digits: ' + result)
