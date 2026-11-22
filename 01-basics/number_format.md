# Formatting Numbers in an F-String


## 1. Why format numbers?

A number can be perfectly fine for calculations but look **unfinished when printed**. If you are showing a price, `7.50` feels more natural than `7.5`.

An f-string lets you **control how a number looks when it is displayed**, without changing the original value. That means you can still use the number in calculations afterwards.

---

## 2. How format specifications work

The general idea is to add a **format specification** after the value inside the braces. The most common one is:

```python
f"{value:.2f}"
```

This displays `value` with **exactly two digits after the decimal point**.

### What each part means

Inside the braces, every character has a role:

| Part | Meaning |
|------|---------|
| `:` | The colon introduces the format specification |
| `.2` | Selects **two decimal places** |
| `f` | Selects **fixed-point** presentation, which shows the number in normal decimal notation |

So `{value:.2f}` reads as: "show `value` as a fixed-point number with 2 decimal places".

### Adding missing zeros

```python
value = 7.5

print(f"{value:.2f}")    # 7.50
print(value)             # 7.5
```

The output shows `7.50` because `.2f` **always** displays two decimal places, so Python pads the result with a trailing zero. The value stored in `value` is still `7.5`.

### Rounding for display

If the number has more decimals than requested, it is **rounded** for display.

```python
value = 9.8765

print(f"{value:.2f}")    # 9.88
print(value)             # 9.8765
```

The display shows `9.88`, but the stored value is untouched.

---

## 3. Formatting produces a string

An f-string always produces a **string**. This is true for the formatted number too.

```python
value = 9.8765
display = f"{value:.2f}"

print(display)           # 9.88
print(value)             # 9.8765

print(type(display))     # <class 'str'>
print(type(value))       # <class 'float'>
```

This means you can save the formatted text in its own variable and still use the original number in calculations. But remember the formatted result is **text**, so you cannot do maths with it. For example, `display * 2` repeats the text instead of doubling the number:

```python
print(display * 2)       # 9.889.88
```

---

## 4. `round()` vs f-string formatting

These two look similar but do different jobs.

- `round(value, 2)` gives a **number** that you can use in further calculations.
- `f"{value:.2f}"` gives a **string** meant for display.

The important difference shows up with trailing zeros. Printing a rounded number uses Python's normal number display, so trailing zeros are **not guaranteed**:

```python
value = 7.5

rounded_value = round(value, 2)
formatted_value = f"{value:.2f}"

print(rounded_value)      # 7.5
print(formatted_value)    # 7.50
```

| | `round(value, 2)` | `f"{value:.2f}"` |
|---|-------------------|------------------|
| Result type | `float` (a number) | `str` (text) |
| Keeps trailing zeros | No | Yes |
| Usable in calculations | Yes | No |
| Best for | Changing the value | Displaying the value |

---

## 5. Formatting doesn't change the underlying value

Some decimal numbers can only be **approximated** as floats, so a calculation can print a surprising result.

```python
total = 0.4 + 0.2

print(total)               # 0.6000000000000001
print(f"{total:.2f}")      # 0.60
```

The f-string **rounds the number for display**, so the output looks clean. But the stored value is unchanged, and any calculation that uses `total` still uses the same floating-point value.

Another example:

```python
total = 1.1 + 2.2

print(total)               # 3.3000000000000003
print(f"{total:.2f}")      # 3.30
print(total == 3.3)        # False
```

Formatting hides the error in the **output only**. The comparison is still `False`, because the underlying number really is `3.3000000000000003`.

---

## 6. A few more format options

The lecture focuses on `.2f`, but the same idea works with other numbers of decimal places and a few other options. These examples are an extra, so you recognize them when you see them.

### Different numbers of decimal places

```python
n = 3.14159

print(f"{n:.0f}")    # 3
print(f"{n:.1f}")    # 3.1
print(f"{n:.3f}")    # 3.142
print(f"{n:.4f}")    # 3.1416
```

`.0f` shows no decimals at all. The number after the dot is how many decimals to display.

### Integers can be shown with decimals too

```python
print(f"{42:.2f}")    # 42.00
```

### A thousands separator

Adding a comma before the dot groups the digits in thousands:

```python
print(f"{1234567.891:,.2f}")    # 1,234,567.89
```

### Percentages

The `%` presentation multiplies by 100 and adds a percent sign:

```python
print(f"{0.256:.1%}")    # 25.6%
```

### Expressions work too

You can put a calculation straight inside the braces and format its result:

```python
price = 19.99
qty = 3

print(f"Total: ${price * qty:.2f}")    # Total: $59.97
```

---

## 7. A note on rounding

Because floats are stored in binary, formatting follows the **actual stored value**, which is sometimes a tiny bit above or below what you typed. A well-known example:

```python
print(f"{2.675:.2f}")    # 2.67
```

You might expect `2.68`, but the stored value of `2.675` is slightly below `2.675`, so it rounds down. This is not a bug. It is the same floating-point approximation described in the numbers lecture.

---

## 8. Why this matters in cybersecurity

- Printing **scan times**, **response times** and **file sizes** in a clean, readable way.
- Showing **percentages**, such as the share of failed logins.
- Creating neat **reports** and **tables** from calculations.
- Displaying results without changing the real values you still need for further checks.

---

## 9. Common mistakes

- Forgetting the **colon**: `{value.2f}` is wrong, it must be `{value:.2f}`.
- Forgetting the **`f`** at the end of the specification.
- Treating the formatted result as a **number**. It is a string.
- Expecting formatting to **change** the original variable. It does not.
- Confusing `round()` (returns a number) with f-string formatting (returns text).
- Assuming `.2f` removes floating-point errors. It only hides them in the output.