# Employee Card Workshop

## Topics covered in this workshop

| Topic | Used in steps |
|-------|---------------|
| Creating strings with single quotes | 1, 4, 16 |
| String concatenation with `+` | 2, 3, 8, 9, 11, 12 |
| Adding a space between strings | 3, 8 |
| Augmented assignment `+=` | 5 |
| String immutability (a new string is created) | 5 |
| Integers stored in variables | 7, 12, 15 |
| `TypeError` when joining a string and an integer | 9, 10 |
| Converting numbers with `str()` | 10, 12 |
| f-strings (string interpolation) | 13, 14, 15 |
| String slicing `string[start:stop]` | 16, 17 |
| Negative indexing and `string[-3:]` | 18 |
| Cleaning up output by removing `print()` calls | 6 |

## What I built

A program that stores an employee's details in variables, builds sentences from them in different ways, and extracts information from an employee code.

| Detail | Variable | Value | Type |
|--------|----------|-------|------|
| First name | `first_name` | `Ali` | `str` |
| Last name | `last_name` | `Raza` | `str` |
| Full name | `full_name` | `Ali Raza` | `str` |
| Address | `address` | `45 Garden Road, Flat 7C` | `str` |
| Age | `employee_age` | `31` | `int` |
| Experience | `experience_years` | `8` | `int` |
| Position | `position` | `Security Analyst` | `str` |
| Salary | `salary` | `90000` | `int` |
| Employee code | `employee_code` | `SEC-2027-AR-042` | `str` |

## Files

| File | Description |
|------|-------------|
| `employee_card.py` | The final program |
| `README.md` | Notes on the 18 steps (this file) |

## How to run

```
python employee_card.py
```

## Output

```
Ali Raza is 31 years old
Experience: 8 years
Employee: Ali Raza | Age: 31 | Position: Security Analyst | Salary: $90000
SEC
2027
AR
042
```

---

## The 18 steps

### Part 1: Creating and joining strings

**Step 1: Create the name variables.**
Strings are sequences of characters used to store text. Created `first_name` and `last_name` and printed both.

```python
first_name = 'Ali'
last_name = 'Raza'
print(first_name)
print(last_name)
```

**Step 2: Concatenate with `+`.**
Combining strings with the `+` operator is called concatenation. Created `full_name` from the two variables and printed it. The result was `AliRaza`, with no space.

```python
full_name = first_name + last_name
```

**Step 3: Add a space.**
Python joins strings exactly as they are, so a space has to be added as its own string (`' '`) between the names.

```python
full_name = first_name + ' ' + last_name     # Ali Raza
```

**Step 4: Create the address.**
Created `address` and printed it.

```python
address = '45 Garden Road'
```

**Step 5: Extend the address with `+=`.**
The `+=` operator adds content to the end of an existing string variable. It is shorter than `address = address + '...'`. Strings are immutable, so this does not change the original string. It creates a new string and reassigns the variable.

```python
address += ', Flat 7C'     # 45 Garden Road, Flat 7C
```

**Step 6: Clean up the output.**
Removed all the `print()` statements so the terminal is not crowded.

### Part 2: Strings and numbers

**Step 7: Add the age.**
Created a variable with an integer value.

```python
employee_age = 31
```

**Step 8: Start a sentence.**
Created `employee_info` by concatenating `full_name` and the string `' is '` (with a space on both sides).

```python
employee_info = full_name + ' is '
```

**Step 9: Concatenate the age, and meet the error.**
Added `employee_age` at the end with `+`. This raised a `TypeError`.

```python
employee_info = full_name + ' is ' + employee_age
```

```
TypeError: can only concatenate str (not "int") to str
```

**Step 10: Fix it with `str()`.**
Python does not allow joining text and numbers directly. The `str()` function returns the string version of a value, so the number must be converted first.

```python
employee_info = full_name + ' is ' + str(employee_age)
```

**Step 11: Finish the sentence and print it.**
Added `' years old'` (starting with a space) at the end and printed the result.

```python
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)      # Ali Raza is 31 years old
```

**Step 12: Use `str()` again.**
Created `experience_years` as an integer, converted it with `str()` and built `experience_info`.

```python
experience_years = 8
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)    # Experience: 8 years
```

### Part 3: f-strings

**Step 13: Create the card with an f-string.**
Joining many strings with `+` and converting numbers with `str()` gets messy. F-strings (introduced in Python 3.6) put the letter `f` before the opening quote and let you place variables and expressions inside curly braces `{}`.

```python
employee_card = f'Employee: {full_name}'
```

**Step 14: Add the age.**
Updated the card to follow the format `Employee: [name] | Age: [age]`. No `str()` is needed inside an f-string.

```python
employee_card = f'Employee: {full_name} | Age: {employee_age}'
```

**Step 15: Add the position and salary.**
Created `position` and `salary`, then extended the card to its final format and printed it.

```python
position = 'Security Analyst'
salary = 90000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
```

```
Employee: Ali Raza | Age: 31 | Position: Security Analyst | Salary: $90000
```

### Part 4: Slicing

**Step 16: Slice from the start.**
Slicing extracts a portion of a string with `string[start:stop]`. The `start` index is included and the `stop` index is excluded. Created `employee_code` and sliced the department from index 0 to 3.

```python
employee_code = 'SEC-2027-AR-042'
department = employee_code[0:3]
print(department)          # SEC
```

**Step 17: Slice from the middle.**
A slice can begin anywhere in the string. Extracted the year and the initials.

```python
year_code = employee_code[4:8]       # 2027
initials = employee_code[9:11]       # AR
print(year_code)
print(initials)
```

**Step 18: Slice from the end.**
Negative indexes count from the end of the string (`-1` is the last character). Leaving out the stop value after the colon means "continue to the end", so `[-3:]` gives the last three characters, which are the ID number.

```python
last_three = employee_code[-3:]
print(last_three)          # 042
```

---

## How the employee code is sliced

| Character | S | E | C | - | 2 | 0 | 2 | 7 | - | A | R | - | 0 | 4 | 2 |
|-----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

- `[0:3]` gives `SEC` (department)
- `[4:8]` gives `2027` (year)
- `[9:11]` gives `AR` (initials)
- `[-3:]` gives `042` (ID number)