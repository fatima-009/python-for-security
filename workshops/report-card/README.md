# Report Card Workshop

A small workshop where I practiced Python data types by creating and printing the data for a simple report card.

## What I built

A short Python program that stores a student's details in variables and prints each value together with its data type:

| Detail | Variable | Data type |
|--------|----------|-----------|
| Student name | `name` | `str` |
| Enrollment status | `is_student` | `bool` |
| Age | `age` | `int` |
| Score | `score` | `float` |

## Files

| File | Description |
|------|-------------|
| `report_card.py` | The final program |
| `README.md` | Notes on the 10 steps (this file) |

## How to run

```
python report_card.py
```

## Output

```
True <class 'bool'>
Sara <class 'str'>
21 <class 'int'>
True
88.5 <class 'float'>
```

---

## The 10 steps

### Step 1: Create the `name` variable
Created a variable called `name` and assigned it a string. A string is a sequence of characters surrounded by single or double quotes.

```python
name = 'Sara'
```

Python uses indentation to organize code, so a line must not start with extra spaces, otherwise an `IndentationError` occurs.

### Step 2: Print the variable
Used the `print()` function to display the value of `name`. `print(name)` is a function call, and `name` is the argument passed to the function. A function is a reusable block of code that runs when it is called.

### Step 3: Check the type with `type()`
Used `type()` to check the data type of `name` and printed the result. The output `<class 'str'>` confirms the value is a string.

### Step 4: Create the `is_student` variable
Declared `is_student` and assigned it the boolean value `True`. Booleans represent a yes-or-no condition and have only two values: `True` and `False`.

```python
is_student = True
```

### Step 5: Print several values on one line
`print()` can display more than one value when they are separated by commas. Printed the value of `is_student` and its type together.

```python
print(is_student, type(is_student))   # True <class 'bool'>
```

### Step 6: Use the same format for the name
Removed the earlier separate outputs for `name` and printed the value and type together, the same way as the previous step.

```python
print(name, type(name))               # Sara <class 'str'>
```

### Step 7: Add the student's age (integer)
Declared `age` as an integer and printed its value and type.

```python
age = 21
print(age, type(age))                 # 21 <class 'int'>
```

### Step 8: Add the score and check it with `isinstance()`
Declared `score` with a decimal value. Used `isinstance()` to check whether it is an `int`. The result was `False`, which shows `score` is not an integer even though it is a number.

```python
score = 88.5
print(isinstance(score, int))         # False
```

### Step 9: Check for `float`
Replaced `int` with `float` in the `isinstance()` call. The result was `True`, confirming that `score` is a float, a number with decimals.

```python
print(isinstance(score, float))       # True
```

### Step 10: Print the score and its type
Completed the report card by printing the `score` value and its data type in a single `print()` statement.

```python
print(score, type(score))             # 88.5 <class 'float'>
```

---

## What I learned

- How to create variables of four basic data types: `str`, `bool`, `int` and `float`.
- How to display values with `print()`, including several values on one line using commas.
- How to check a value's type with `type()`.
- How to test a type with `isinstance()`, which returns `True` or `False`.
- That two numbers can have different types (`int` and `float`).
- That Python uses indentation, so lines must not start with extra spaces.