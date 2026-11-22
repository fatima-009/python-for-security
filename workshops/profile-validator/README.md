# Employee Profile Validator Workshop

A workshop in which I practiced Python's string methods by cleaning, checking and extracting data from an employee profile (emails, names, phone numbers, addresses and employee codes).

## Topics covered in this workshop

| Topic | Used in steps |
|-------|---------------|
| f-strings for formatted output | 2 to 22 |
| `.find()` to locate a character | 3, 13 |
| Slicing with `string[:index]` | 4, 13 |
| The `in` keyword (membership check) | 5, 6 |
| Handling messy data (extra spaces, wrong casing) | 7, 8 |
| `.title()` | 9, 10, 14 |
| `.strip()` | 10, 11 |
| Method chaining (`.strip().title()`, `.strip().lower()`) | 10, 11, 14 |
| `.lower()` | 11 |
| `.upper()` | 12 |
| `.replace(old, new)` | 14, 15 |
| `.split(separator)` | 16 |
| `.join(list)` | 17 |
| `.startswith()` | 18, 20 |
| `.endswith()` | 19, 20 |
| `.count()` | 21, 22 |

## What I built

A program that takes raw, messy employee data and turns it into clean, validated information.

| Task | Input | Result |
|------|-------|--------|
| Find the `@` position | `omar.farooq@techcorp.com` | `11` |
| Extract the username | `omar.farooq@techcorp.com` | `omar.farooq` |
| Clean a name | `'  hAMzA mALIK  '` | `'Hamza Malik'` |
| Clean an email | `'  HAMZA.MALIK@TECHCORP.COM  '` | `'hamza.malik@techcorp.com'` |
| Make a name badge | `Hamza Malik` | `HAMZA MALIK` |
| Make a display name | `hamza.malik` | `Hamza Malik` |
| Remove dashes from a phone number | `300-765-4321` | `3007654321` |
| Split an address | `45 Garden Road, Lahore, PB` | `['45 Garden Road', 'Lahore', 'PB']` |
| Check an employee code | `EMP-2026-HM` | starts with `EMP`: `True` |
| Count characters | `hamza.malik@techcorp.com` | 2 dots |

## Files

| File | Description |
|------|-------------|
| `profile_validator.py` | The final program |
| `README.md` | Notes on the 22 steps (this file) |

## How to run

```
python profile_validator.py
```

## Output

```
Email: omar.farooq@techcorp.com
Position of @: 11
Username: omar.farooq
Has @ symbol: True
Has .com: True
Original name: '  hAMzA mALIK  '
Cleaned name: 'Hamza Malik'
Original email: '  HAMZA.MALIK@TECHCORP.COM  '
Cleaned email: 'hamza.malik@techcorp.com'
Name badge: HAMZA MALIK
Email: hamza.malik@techcorp.com
Username: hamza.malik
Display name: Hamza Malik
Phone with dashes: 300-765-4321
Phone without dashes: 3007654321
Address parts: ['45 Garden Road', 'Lahore', 'PB']
Rejoined: 45 Garden Road | Lahore | PB
Code: EMP-2026-HM
Starts with EMP: True
Clean email: hamza.malik@techcorp.com
Ends with .com: True
Dots in email: 2
Dashes in code: 2
```

---

## The 22 steps

### Part 1: Finding and extracting (steps 1 to 6)

**Step 1: Create the email variable.**
Started the workshop by creating a variable that stores an email address.

```python
email = 'omar.farooq@techcorp.com'
```

**Step 2: Print with an f-string.**
An f-string starts with `f` before the opening quote, and variables go inside `{}`.

```python
print(f'Email: {email}')       # Email: omar.farooq@techcorp.com
```

**Step 3: Find a character with `.find()`.**
The `.find()` method returns the index (position) of the first occurrence of a substring. Used it to find the position of the `@` sign.

```python
at_position = email.find('@')
print(f'Position of @: {at_position}')    # Position of @: 11
```

**Step 4: Extract the username with slicing.**
The username is everything before the `@`, so a slice from the start up to `at_position` gives it. The stop index is excluded, so the `@` itself is not included.

```python
username = email[:at_position]
print(f'Username: {username}')    # Username: omar.farooq
```

**Step 5: Check for a character with `in`.**
The `in` keyword returns `True` if a substring exists inside a string, and `False` otherwise.

```python
has_at = '@' in email
print(f'Has @ symbol: {has_at}')    # Has @ symbol: True
```

**Step 6: Check for `.com`.**
Used `in` again with a longer substring.

```python
has_com = '.com' in email
print(f'Has .com: {has_com}')       # Has .com: True
```

### Part 2: Cleaning messy text (steps 7 to 12)

**Step 7: Create messy data.**
Real-world data often has extra spaces and inconsistent casing. Created a name with two spaces at the start, two at the end, and mixed capital letters.

```python
messy_name = '  hAMzA mALIK  '
```

**Step 8: Print with visible quotes.**
Wrapped the name in single quotes inside the output so the leading and trailing spaces can be seen.

```python
print(f"Original name: '{messy_name}'")
# Original name: '  hAMzA mALIK  '
```

**Step 9: Capitalize with `.title()`.**
The `.title()` method capitalizes the first letter of each word and lowercases the rest. Stored the result in `clean_name`. The spaces were still there at this point.

```python
clean_name = messy_name.title()
```

**Step 10: Chain `.strip()` and `.title()`.**
The `.strip()` method removes whitespace from both ends. Methods can be chained, and each one works on the result of the previous call. Here `.title()` operates on the string returned by `.strip()`.

```python
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")
# Cleaned name: 'Hamza Malik'
```

**Step 11: Normalize an email with `.lower()`.**
The `.lower()` method converts everything to lowercase, which is useful for comparing and storing emails. Combined it with `.strip()`.

```python
messy_email = '  HAMZA.MALIK@TECHCORP.COM  '
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")
# Original email: '  HAMZA.MALIK@TECHCORP.COM  '
# Cleaned email: 'hamza.malik@techcorp.com'
```

**Step 12: Make a name badge with `.upper()`.**
The `.upper()` method converts all characters to uppercase.

```python
name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')    # Name badge: HAMZA MALIK
```

### Part 3: Reusing and replacing (steps 13 to 15)

**Step 13: Repeat the technique on the clean email.**
Used `.find()` and slicing again, this time on `clean_email`.

```python
at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]
print(f'Email: {clean_email}')       # Email: hamza.malik@techcorp.com
print(f'Username: {email_user}')     # Username: hamza.malik
```

**Step 14: Replace characters with `.replace()`.**
The `.replace(old, new)` method replaces every occurrence of `old` with `new`. Replaced the dot with a space, then chained `.title()` to build a readable display name.

```python
display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')    # Display name: Hamza Malik
```

**Step 15: Remove unwanted characters.**
Replacing with an empty string deletes the character. Removed the dashes from a phone number.

```python
phone = '300-765-4321'
phone_clean = phone.replace('-', '')
print(f'Phone with dashes: {phone}')           # 300-765-4321
print(f'Phone without dashes: {phone_clean}')  # 3007654321
```

### Part 4: Splitting and joining (steps 16 and 17)

**Step 16: Split a string with `.split()`.**
The `.split(separator)` method splits a string at each occurrence of the separator and returns a list. Split the address on a comma followed by a space.

```python
full_address = '45 Garden Road, Lahore, PB'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')
# Address parts: ['45 Garden Road', 'Lahore', 'PB']
```

**Step 17: Join a list with `.join()`.**
The `.join()` method is the opposite of `.split()`. The separator goes before the dot, and the list goes inside the parentheses.

```python
rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')
# Rejoined: 45 Garden Road | Lahore | PB
```

### Part 5: Checking the start and end (steps 18 to 20)

**Step 18: `.startswith()`.**
Returns `True` if the string begins with the given prefix, otherwise `False`.

```python
employee_code = 'EMP-2026-HM'
starts_with_emp = employee_code.startswith('EMP')
```

**Step 19: `.endswith()`.**
Returns `True` if the string ends with the given suffix, otherwise `False`.

```python
ends_with_com = clean_email.endswith('.com')
```

**Step 20: Print the checks.**

```python
print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')
```

```
Code: EMP-2026-HM
Starts with EMP: True
Clean email: hamza.malik@techcorp.com
Ends with .com: True
```

### Part 6: Counting (steps 21 and 22)

**Step 21: Count with `.count()`.**
The `.count(substring)` method returns the number of non-overlapping occurrences of a substring.

```python
dot_count = clean_email.count('.')
dash_count = employee_code.count('-')
```

**Step 22: Print the counts.**

```python
print(f'Dots in email: {dot_count}')       # Dots in email: 2
print(f'Dashes in code: {dash_count}')     # Dashes in code: 2
```

---

## How the cleaning chain works

```
'  hAMzA mALIK  '
        |  .strip()
'hAMzA mALIK'
        |  .title()
'Hamza Malik'
```

Methods in a chain run from left to right, and each one receives the string returned by the one before it. The original variable is never changed, because strings are immutable. Every method returns a new string.
