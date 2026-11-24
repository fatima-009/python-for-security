# Movie Ticket Booking Calculator Workshop

A workshop in which I practiced booleans and conditional statements by building a movie ticket booking calculator. The program checks whether a user can book a ticket, applies a membership discount, adds extra and service charges, and calculates the final price.

## Topics covered in this workshop

| Topic | Used in steps |
|-------|---------------|
| Integer, string and boolean variables | 1, 2, 6, 7 |
| `if` statements | 3, 4 |
| Comparison operators `>`, `>=` | 3, 4, 10, 15, 16, 17 |
| `if...else` statements | 5, 9, 13, 15 |
| Truthiness (`if is_member:`) | 8 |
| `.2f` formatting in f-strings | 9, 13, 20, 21 |
| Boolean operator `and` | 10, 16 |
| Equality operator `==` | 12 |
| Boolean operator `or` | 14, 16, 17 |
| Inequality operator `!=` | 16, 17 |
| Operator precedence (`and` before `or`) | 16 |
| Parentheses to group conditions | 17 |
| Nested `if` statements | 18, 19, 20 |
| `if...elif...else` | 20 |
| Arithmetic with `+` and `-` | 21 |

## What I built

A calculator that decides whether a user can book a ticket and works out the final price.

| Detail | Variable | Value | Type |
|--------|----------|-------|------|
| Base price of the ticket | `base_price` | `18` | `int` |
| Age of the user | `age` | `19` | `int` |
| Seat type | `seat_type` | `'Premium'` | `str` |
| Show time | `show_time` | `'Matinee'` | `str` |
| Is the user a member? | `is_member` | `False` | `bool` |
| Is the show on a weekend? | `is_weekend` | `True` | `bool` |
| Membership discount | `discount` | `0` | `int` |
| Extra charges | `extra_charges` | `0` (then `2`) | `int` |
| Service charges | `service_charges` | `0` (then `5`) | `int` |

## Files

| File | Description |
|------|-------------|
| `ticket_calculator.py` | The final program |
| `README.md` | Notes on the 21 steps (this file) |

## How to run

```
python ticket_calculator.py
```

## Output

```
User is eligible to book a ticket
User is not eligible for Evening shows
User does not qualify for membership discount
Discount: 0.00
Extra charges will be applied
Extra charges: 2.00
Ticket booking condition satisfied
Service charges: 5.00
Final price of ticket: 25.00
```

The final price is `18 + 2 + 5 - 0 = 25.00`: the base price, plus extra charges (it is a weekend), plus service charges (Premium seat), minus the discount (none, because the user is not a member).

---

## The 21 steps

### Part 1: Declaring the data (steps 1 and 2)

**Step 1: Numbers about the user and the show.**
Created the base price and the user's age.

```python
base_price = 18
age = 19
```

**Step 2: Strings about the ticket.**
Stored the seat type and the show time as strings.

```python
seat_type = 'Premium'
show_time = 'Matinee'
```

### Part 2: Simple conditions (steps 3 to 5)

**Step 3: An `if` statement.**
An `if` statement runs its indented body only when the condition is true. The greater than operator `>` gives `True` when the left value is bigger than the right value. Checked whether the user is old enough.

```python
if age > 17:
    print('User is eligible to book a ticket')
```

**Step 4: Greater than or equal to.**
The `>=` operator is also `True` when the two values are equal, unlike `>`. Checked whether the user can book an evening show.

```python
if age >= 21:
    print('User is eligible for Evening shows')
```

**Step 5: Add an `else` clause.**
The `else` clause handles the case when the condition is false.

```python
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')
```

```
User is not eligible for Evening shows
```

### Part 3: Booleans and the discount (steps 6 to 11)

**Step 6: Boolean variables.**
Some information is only true or false. Booleans are written without quotes. At this stage the user is a member.

```python
is_member = True
is_weekend = True
```

**Step 7: The discount.**
Created a variable for the discount that starts at `0`.

```python
discount = 0
```

**Step 8: Truthiness.**
An `if` condition does not have to compare a value with `True` or `False`. It uses the **truthiness** of the value. Truthy values include `True`, non-zero numbers and non-empty strings. Used `is_member` directly as the condition.

```python
if is_member:
    discount = 3
    print('User qualifies for membership discount')
```

**Step 9: `else` and `.2f` formatting.**
Added an `else` clause, then printed the discount with two decimal places. The `.2f` format works with integers too, so `3` is displayed as `3.00`.

```python
if is_member:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print(f'Discount: {discount:.2f}')
```

```
User qualifies for membership discount
Discount: 3.00
```

**Step 10: The `and` operator.**
`and` requires all the conditions to be true. The discount should apply only to members who are 21 or older.

```python
if is_member and age >= 21:
```

Since the age is 19, the condition is now false even for a member:

```
User does not qualify for membership discount
Discount: 0.00
```

**Step 11: Not a member.**
Changed `is_member` to `False`. The discount stays `0`, because **both** conditions must be satisfied.

```python
is_member = False
```

### Part 4: Extra charges (steps 12 to 14)

**Step 12: The equality operator `==`.**
`==` checks whether two values are equal. It is different from `=`, which assigns a value. Created `extra_charges` and added a charge for evening shows.

```python
extra_charges = 0

if show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
```

**Step 13: `else` and the printed amount.**

```python
else:
    print('No extra charges will be applied')
print(f'Extra charges: {extra_charges:.2f}')
```

**Step 14: The `or` operator.**
`or` requires at least one condition to be true. Extra charges should also apply on weekends.

```python
if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print(f'Extra charges: {extra_charges:.2f}')
```

```
Extra charges will be applied
Extra charges: 2.00
```

The show is a `Matinee`, but it is on a weekend, so the second condition makes the whole expression true.

### Part 5: The booking rules (steps 15 to 17)

**Step 15: Users aged 21 or older.**
Users aged 21 or above can always book.

```python
if age >= 21:
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')
```

**Step 16: Users aged 18 to 20, but not for evening shows.**
The inequality operator `!=` is `True` when two values are different. When `and` and `or` appear in the same expression, **`and` has a higher precedence**, so the conditions joined with `and` are grouped together, as if in parentheses.

```python
if age >= 21 or age >= 18 and show_time != 'Evening':
```

This is read as `age >= 21 or (age >= 18 and show_time != 'Evening')`.

**Step 17: Evening shows for members.**
Users aged 18 to 20 can also book evening shows if they are members. Parentheses `()` change the grouping, so `show_time != 'Evening'` and `is_member` are checked together.

```python
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')
```

```
Ticket booking condition satisfied
```

The user is 19 and the show is not in the evening, so the booking is allowed.

### Part 6: Service charges and the final price (steps 18 to 21)

**Step 18: A nested `if`.**
An `if` placed inside another `if` is a **nested `if`**. The inner `if` runs only when the outer condition is true. Inside the outer `if` body, created `service_charges` and checked the seat type.

```python
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
```

**Step 19: Add an `else`.**

```python
    else:
        service_charges = 1
```

**Step 20: `if...elif...else`.**
The `elif` clause checks another condition when the first is false. Added a check for `Gold` seats and printed the service charges.

```python
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print(f'Service charges: {service_charges:.2f}')
```

```
Service charges: 5.00
```

**Step 21: The final price.**
The final price is the base price, plus the extra charges and service charges, minus the discount. The `+` and `-` operators can be combined in one expression.

```python
    final_price = base_price + extra_charges + service_charges - discount
    print(f'Final price of ticket: {final_price:.2f}')
```

```
Final price of ticket: 25.00
```

---

## How the booking condition works

```python
age >= 21 or age >= 18 and (show_time != 'Evening' or is_member)
```

Python groups it like this:

```
age >= 21
  or
(age >= 18 and (show_time != 'Evening' or is_member))
```

| Age | Show time | Member | Can book? | Why |
|-----|-----------|--------|-----------|-----|
| 21 or more | Any | Any | Yes | First part is true |
| 18 to 20 | Not evening | Any | Yes | Old enough, and not an evening show |
| 18 to 20 | Evening | Yes | Yes | Evening shows are allowed for members |
| 18 to 20 | Evening | No | No | Evening show and not a member |
| Under 18 | Any | Any | No | Too young |

---

## Testing different inputs

I tested the program by changing the variables and checking each result.

| Age | Show | Member | Weekend | Seat | Result |
|-----|------|--------|---------|------|--------|
| 19 | Matinee | No | Yes | Premium | Booked. Final price `25.00` |
| 19 | Evening | No | No | Gold | `Ticket booking failed due to restrictions` |
| 19 | Evening | Yes | No | Gold | Booked. Final price `23.00` |
| 16 | Matinee | No | No | Gold | `Ticket booking failed due to restrictions` |
| 24 | Evening | No | No | Standard | Booked. Final price `21.00` |
| 24 | Evening | Yes | No | Premium | Booked with discount. Final price `22.00` |
| 18 | Matinee | No | No | Standard | Booked. Final price `19.00` |
| 20 | Evening | Yes | Yes | Premium | Booked, no discount (under 21). Final price `25.00` |
