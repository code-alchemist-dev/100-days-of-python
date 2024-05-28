print('Tip Calculator!!!\n')

# Collecting inputs from the user
bill_amount = float(input('Enter total bill: R '))
tip = float(input('Enter tip percentage: '))
number_of_people = int(input('Enter total number of people: '))

# Calculating the total amount to be paid per person
tip_amount = round(tip / 100 * bill_amount, 2)
total_bill_amount = round(bill_amount + tip_amount, 2)
total_amount_per_person = round(total_bill_amount / number_of_people, 2)

print('\n')

# Displaying results
print(f'Bill amount: R {bill_amount}')
print(f'Total tip amount: R {tip_amount}\n')
print(f'Total bill amount: R {total_bill_amount}')
print(f'Total amount per person: R {total_amount_per_person}')
