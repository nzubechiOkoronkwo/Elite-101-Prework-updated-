print('Welcome to your food delivery ChatBot!')
user_name = input('Please enter your name: ')
user_age = input(f'Nice to meet you, {user_name}. How old are you? ')
print(f'Welcome {user_name}. How can I help? ')
print() 
print('''
1. Track My Order
2. Report a Delay
3. Contact Delivery Driver
4. Request Refund
5. Order History
6. Support Chat
''')
help_user = int(input('Please choose from the options below: '))
if help_user == 1: 
    print("Your order is at this location")
elif help_user == 2:
    print('Your delay has been reported ')
elif help_user == 3:
    print('Calling delievery driver...')
elif help_user == 4:
    print('Your money will be refunded in 3 business days.')
elif help_user == 5:
    print('Here is your order history')
elif help_user == 6:
    print('Connecting to a live agent')
else: 
    print('Invalid entry. Please choose from the options above.')
