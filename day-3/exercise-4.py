print('Love Compatibility Calculator!!!\n')  # Prints the title of the program.

# Get the user's full name and their partner's full name, then concatenate them and convert to lowercase.
string_name = input('Please enter your full name: ')
string_name = (string_name + input('Please enter your partner\'s full name: ')).lower()

# Count the occurrences of the letters 't', 'r', 'u', 'e' in the concatenated string.
t = string_name.count('t')
r = string_name.count('r')
u = string_name.count('u')
e = string_name.count('e')

# Count the occurrences of the letters 'l', 'o', 'v', 'e' in the concatenated string.
l = string_name.count('l')
o = string_name.count('o')
v = string_name.count('v')
_e = string_name.count('e')

# Combine the counts of 't', 'r', 'u', 'e' to form the first digit, and 'l', 'o', 'v', 'e' to form the second digit.
total = int(str((t + r + u + e)) + str((l + o + v + _e)))

# Determine the compatibility message based on the total score.
if total < 10 or total > 90:
    # If the score is less than 10 or greater than 90, print a message indicating a strong but explosive relationship.
    print(f'Your score is {total}, you go together like coke and mentos.')
elif total >= 40 and total <= 50:
    # If the score is between 40 and 50 inclusive, print a message indicating a moderately good relationship.
    print(f'Your score is {total}, you are alright together.')
else:
    # For all other scores, simply print the score.
    print(f'Your score is {total}')
