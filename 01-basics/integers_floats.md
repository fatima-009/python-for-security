# Working with Integers and Floating Point Numbers


## 1. Numeric data types

Integers and floats are the two **primary numeric data types** in Python. With them you can store numbers and perform mathematical operations.

| Type | Meaning | Examples |
|------|---------|----------|
| `int` | Whole numbers without a decimal point (positive, negative or zero) | `84`, `-9`, `0` |
| `float` | Numbers in floating-point form, written with a decimal point | `3.14`, `-7.0`, `0.0` |

---

## 2. Working with integers

An **integer** is a whole number. It can be positive, negative or zero.

```python
my_int_1 = 84
my_int_2 = -9

print(type(my_int_1))    # <class 'int'>
print(type(my_int_2))    # <class 'int'>
```

Python integers can be as large as memory allows, so there is no overflow problem.

### Arithmetic with integers

```python
x = 84
y = 15

print('Integer Addition:', x + y)          # Integer Addition: 99
print('Integer Subtraction:', x - y)       # Integer Subtraction: 69
print('Integer Multiplication:', 15 * 6)   # Integer Multiplication: 90
print('Division:', 50 / 15)                # Division: 3.3333333333333335
```

| Operator | Operation |
|----------|-----------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |

### Division always gives a float

Notice that dividing two integers with `/` gives a **float** result, even when the answer is a whole number:

```python
print(20 / 5)          # 4.0
print(type(20 / 5))    # <class 'float'>
```

---

## 3. Working with floats

A **float** represents a number in floating-point form, such as `3.14`, `-0.5` or `0.0`. A number is a float as soon as it has a decimal point, even if the decimal part is zero (`-7.0` is a float).

```python
my_float_1 = -7.0
my_float_2 = 3.6

print(type(my_float_1))    # <class 'float'>
print(type(my_float_2))    # <class 'float'>
```

### Arithmetic with floats

```python
p = 2.2
q = 8.0

print('Float Addition:', p + q)          # Float Addition: 10.2
print('Float Subtraction:', q - p)       # Float Subtraction: 5.8
print('Float Multiplication:', q * p)    # Float Multiplication: 17.6
print('Float Division:', q / p)          # Float Division: 3.6363636363636362
```

The same operators (`+`, `-`, `*`, `/`) work with floats. Division often produces a long string of decimal digits.

---

## 4. Mixing integers and floats

When you combine an integer and a float in an operation, Python automatically gives you a **float**.

```python
result = 40 + 2.5

print(result)          # 42.5
print(type(result))    # <class 'float'>
```

This is true for subtraction, multiplication and division too. Even when the answer looks like a whole number, the type is still float:

```python
print(40 * 2.5)          # 100.0
print(type(40 * 2.5))    # <class 'float'>
```

---

## 5. More arithmetic operators

Besides the basic four, Python has three more operators. They work with both integers and floats.

### Modulo `%`: the remainder

The **modulo** operator returns the **remainder** when the left value is divided by the right value.

```python
print(50 % 15)       # 5
print(8.0 % 2.5)     # 0.5
```

`50` divided by `15` goes in 3 times (`45`) with `5` left over, so the result is `5`. Modulo is often used to check whether a number is even or odd (`n % 2`) or divisible by another number (the result is `0`).

### Floor division `//`

**Floor division** divides two numbers and returns the **greatest integer less than or equal to the result**. It is written with a double forward slash.

```python
print(50 // 15)      # 3
print(8.0 // 2.5)    # 3.0
```

With integers the result is an integer. With floats the result is a float (`3.0`), but it is still rounded **down** to a whole value.

### Exponentiation `**`

**Exponentiation** raises a number to a power. It is written with a double asterisk.

```python
print(7 ** 20)       # 79792266297612001
print(2.5 ** 4.0)    # 39.0625
```

`7 ** 20` means 7 multiplied by itself 20 times. Notice how large integer results can get without any error.

### A detail about negative numbers

Floor division rounds **down**, which means toward negative infinity, not toward zero:

```python
print(-7 // 2)       # -4
print(-7 % 3)        # 2
```

`-7 / 2` is `-3.5`, and the greatest integer less than or equal to it is `-4`, not `-3`.

### Summary of operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `84 + 15` | `99` |
| `-` | Subtraction | `84 - 15` | `69` |
| `*` | Multiplication | `15 * 6` | `90` |
| `/` | Division | `50 / 15` | `3.3333333333333335` |
| `%` | Modulo (remainder) | `50 % 15` | `5` |
| `//` | Floor division | `50 // 15` | `3` |
| `**` | Exponentiation | `7 ** 20` | `79792266297612001` |

---

## 6. Floating point representation and rounding errors

Sometimes a float calculation gives **more decimal digits than expected**.

```python
print(1.1 + 2.2)    # 3.3000000000000003
print(0.1 * 3)      # 0.30000000000000004
```

### Why does this happen?

Computers store numbers in **binary** (base 2). Some decimal fractions cannot be written exactly in binary, so they are stored as **finite approximations**. This is similar to how the fraction `1/3` cannot be written exactly in decimal: it becomes `0.33333...` and has to be cut off somewhere.

The result is a tiny **rounding error**. This is normal in almost every programming language, not a bug in Python.

### What to do about it

- Do not rely on floats being exactly equal after calculations.
- Use `round()` to display a cleaner number (see section 8).
- Use integers for exact values when possible, for example storing money as whole cents.

---

## 7. Converting data into integers or floats

Python provides built-in functions to convert numbers and strings into other numeric types.

### `float()`

Returns a **floating-point** number built from the given value.

```python
my_int = 40
my_float = float(my_int)

print(my_float)          # 40.0
print(type(my_float))    # <class 'float'>
```

### `int()`

Returns an **integer** built from the given value. When converting a float, the decimal part is **cut off** (truncated), not rounded.

```python
my_float = 9.87
my_int = int(my_float)

print(my_int)            # 9
print(type(my_int))      # <class 'int'>
print(int(-9.87))        # -9
```

`int()` truncates toward zero, so `9.87` becomes `9` (not `10`) and `-9.87` becomes `-9`.

### Converting strings

The same functions can convert **strings** into numbers. This is very important, because data from users and files arrives as text.

```python
converted_int = int('120')
converted_float = float('3.5')

print(converted_int, type(converted_int))      # 120 <class 'int'>
print(converted_float, type(converted_float))  # 3.5 <class 'float'>
```

The text must look like a valid number for the chosen type. For example, `int('3.5')` fails because `3.5` is not a whole number:

```
ValueError: invalid literal for int() with base 10: '3.5'
```

To convert text like `'3.5'`, use `float()` first.

### Infinity with `float('inf')`

Passing the string `'inf'` to `float()` creates a special value representing **positive infinity**. It is greater than any finite integer or float.

```python
infinity = float('inf')

print(infinity)                 # inf
print(type(infinity))           # <class 'float'>
print(infinity > 10 ** 100)     # True
```

This is useful as a starting value that is guaranteed to be larger than anything you will compare it with, for example when searching for the smallest number in a group.

---

## 8. Other useful functions

### `round()`

Rounds a number to the given number of decimal places. With **no second argument**, it rounds to the nearest integer and returns a whole number.

```python
print(round(6.789))        # 7
print(round(6.234, 2))     # 6.23
```

- `round(6.789)` gives the integer `7`.
- `round(6.234, 2)` keeps 2 decimal places and gives `6.23`.

One surprise: when a number is exactly halfway, Python rounds to the nearest **even** number.

```python
print(round(2.5))    # 2
print(round(3.5))    # 4
```

### `abs()`

Returns the **absolute value** of a number, which is its distance from zero (always positive or zero).

```python
print(abs(-42))      # 42
print(abs(-3.5))     # 3.5
```

### `pow()`

Raises a number to a power, like `**`. With a **third argument** it performs **modular exponentiation**, meaning the result of the power is divided by that number and the remainder is returned.

```python
print(pow(3, 4))       # 81    (same as 3 ** 4)
print(pow(3, 4, 5))    # 1     (same as (3 ** 4) % 5)
```

Modular exponentiation is used a lot in **cryptography**, so it is good to know it exists.

---

## 9. Why this matters in cybersecurity

- **Port numbers** and **counts** (failed logins, packets) are integers.
- **Response times** and **percentages** are often floats.
- Converting text from logs or user input with `int()` and `float()`.
- **Modulo** is used in many algorithms, such as simple ciphers, hashing and checking even or odd values.
- **Modular exponentiation** with `pow()` is a building block of public-key cryptography such as RSA.
- Understanding **rounding errors** helps avoid wrong comparisons in calculations.

---

## 10. Common mistakes

- Expecting `/` to return an integer. It always returns a float.
- Expecting `int()` to **round**. It truncates.
- Comparing floats with `==` after calculations, because of rounding errors.
- Using `int()` directly on text like `'3.5'`.
- Confusing `//` (floor division) with `/` (normal division).
- Confusing `**` (power) with `*` (multiplication).
- Forgetting that `round()` has an optional second argument for decimal places.
