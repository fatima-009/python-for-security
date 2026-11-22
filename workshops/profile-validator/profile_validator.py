# Employee Profile Validator Workshop
# Practicing Python string methods

# Steps 1-2: create the email and print it with an f-string
email = 'omar.farooq@techcorp.com'
print(f'Email: {email}')

# Step 3: find() returns the index of the first match
at_position = email.find('@')
print(f'Position of @: {at_position}')

# Step 4: slicing - everything before the @ sign
username = email[:at_position]
print(f'Username: {username}')

# Steps 5-6: the "in" keyword returns True or False
has_at = '@' in email
print(f'Has @ symbol: {has_at}')

has_com = '.com' in email
print(f'Has .com: {has_com}')

# Steps 7-10: cleaning messy text with strip() and title()
messy_name = '  hAMzA mALIK  '
print(f"Original name: '{messy_name}'")

clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

# Step 11: normalizing an email with strip() and lower()
messy_email = '  HAMZA.MALIK@TECHCORP.COM  '
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

# Step 12: upper() for a name badge
name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')

# Step 13: find() and slicing on the cleaned email
at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]
print(f'Email: {clean_email}')
print(f'Username: {email_user}')

# Step 14: replace() and title() chained
display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')

# Step 15: replace() to remove unwanted characters
phone = '300-765-4321'
phone_clean = phone.replace('-', '')
print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')

# Step 16: split() turns a string into a list
full_address = '45 Garden Road, Lahore, PB'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')

# Step 17: join() turns a list back into a string
rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

# Steps 18-20: startswith() and endswith() checks
employee_code = 'EMP-2026-HM'
starts_with_emp = employee_code.startswith('EMP')
ends_with_com = clean_email.endswith('.com')
print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')

# Steps 21-22: count() counts occurrences
dot_count = clean_email.count('.')
dash_count = employee_code.count('-')
print(f'Dots in email: {dot_count}')
print(f'Dashes in code: {dash_count}')