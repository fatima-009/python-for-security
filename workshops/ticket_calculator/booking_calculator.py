# Movie Ticket Booking Calculator Workshop
# Practicing booleans and conditional statements

# Steps 1-2: information about the user and the show
base_price = 18
age = 19
seat_type = 'Premium'
show_time = 'Matinee'

# Step 3: check if the user is old enough to book a ticket
if age > 17:
    print('User is eligible to book a ticket')

# Steps 4-5: check if the user can book an evening show (if...else)
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# Step 6: boolean variables (step 11 changes is_member to False)
is_member = False
is_weekend = True

# Step 7: the discount starts at 0
discount = 0

# Steps 8-10: membership discount (truthiness and the "and" operator)
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print(f'Discount: {discount:.2f}')

# Steps 12-14: extra charges for evening shows or weekends (the "or" operator)
extra_charges = 0
if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print(f'Extra charges: {extra_charges:.2f}')

# Steps 15-17: booking rules (precedence of "and" over "or", and parentheses)
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    # Steps 18-20: service charges with a nested if...elif...else
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print(f'Service charges: {service_charges:.2f}')

    # Step 21: the final price
    final_price = base_price + extra_charges + service_charges - discount
    print(f'Final price of ticket: {final_price:.2f}')
else:
    print('Ticket booking failed due to restrictions')