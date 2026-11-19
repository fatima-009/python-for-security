# Employee Card Workshop
# Practicing Python strings: creating, concatenation, f-strings and slicing

# Steps 1-3: first name, last name and full name (concatenation with a space)
first_name = 'Ali'
last_name = 'Raza'
full_name = first_name + ' ' + last_name

# Steps 4-5: address, extended with += (creates a new string)
address = '45 Garden Road'
address += ', Flat 7C'

# Step 7: age (integer)
employee_age = 31

# Steps 8-11: build a sentence; numbers must be converted with str()
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

# Step 12: experience, converted with str() before concatenating
experience_years = 8
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# Steps 13-15: employee card with an f-string (no str() needed)
position = 'Security Analyst'
salary = 90000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# Steps 16-18: slicing the employee code
employee_code = 'SEC-2027-AR-042'

department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)

last_three = employee_code[-3:]
print(last_three)