# String Interpolation (f-strings)

## 1. What is string interpolation?

**String interpolation** is the process of **inserting variables and expressions into a string**. Instead of cutting the text into pieces and joining them with `+`, you write the sentence once and mark the places where values should go.

Python's tool for this is the **f-string**, short for *formatted string literal*.

---

## 2. How f-strings work

- Put the letter **`f`** (lowercase or uppercase) **before the opening quote**.
- Inside the string, put variables or expressions in **curly braces `{}`**. These are called **replacement fields**.
- Python replaces each pair of braces with the value.

```python
city = 'Lahore'
temp = 28

print(f'It is {temp} degrees in {city}')
# It is 28 degrees in Lahore
```

Uppercase `F` works exactly the same way:

```python
print(F'Capital F works: {city}')
# Capital F works: Lahore
```

---

## 3. Expressions inside the braces

The braces can hold full **expressions**, not just variable names. Python calculates the expression first and then inserts the result.

```python
a = 7
b = 3

print(f'The product of {a} and {b} is {a * b}')
# The product of 7 and 3 is 21
```

You can also call methods and functions inside the braces:

```python
print(f'{city.upper()} has {len(city)} letters')
# LAHORE has 6 letters
```

---

## 4. No `str()` needed

With f-strings you do **not** need to convert numbers into strings. Python converts the values to strings for you during interpolation. That is why the examples above work with integers (`temp`, `a`, `b`) without any error.

This solves the `TypeError` you get when joining a string and a number with `+`.

---

## 5. Interpolation vs concatenation

| | Concatenation (`+`) | f-string |
|---|---------------------|----------|
| Syntax | `'Hello ' + name` | `f'Hello {name}'` |
| Works with numbers directly | No, needs `str()` | Yes |
| Adds spaces automatically | No | No, you write them in the text |
| Readability with many parts | Gets messy | Clean and compact |
| Can contain expressions | No | Yes |

Both are valid. Concatenation is fine for joining two or three simple strings, while f-strings are usually clearer when the text contains several values. In modern Python, f-strings are the preferred way to build formatted text.

---

## 6. Why this matters in cybersecurity

- Writing readable **log messages**, such as a failed-login report with a username and the attempt count.
- Printing **scan results**, such as `f'Port {port} is {status}'`.
- Building **URLs** and **commands** from several values.
- Showing the result of a **calculation** right inside a message.

---

## 7. Common mistakes

- Forgetting the `f` before the quotes. Without it, the braces are printed as plain text.
- Misspelling a variable name inside the braces (`NameError`).
- Forgetting spaces in the text around the braces.
- Putting very long or complicated expressions inside the braces. Calculate them first in a variable to keep the code readable.