# Truthy and Falsy Values, Boolean Operators and Short-Circuiting


## 1. Why do we need more than one condition?

In the previous lesson you used comparison operators and `if` statements to control the flow of a program. But often you need to **check several things at once**. One way is to **nest** one `if` inside another:

```python
is_registered = True
age = 30

if is_registered:
    if age >= 21:
        print('You can enter the event')    # You can enter the event
    else:
        print('You are too young to enter')
else:
    print('Please register first')
```

This first checks `is_registered`. If it is `True`, it moves to the inner `if` and checks `age`. It works, but with more conditions the nesting quickly becomes long and hard to read.

For more complex conditions, Python provides the operators **`and`**, **`or`** and **`not`**. To understand them properly, you first need to know about **truthy and falsy values**.

---

## 2. Truthy and falsy values

In Python, **every value has an inherent boolean value**: a built-in sense of whether it should be treated as `True` or `False` in a logical context.

- **Truthy** values are treated as `True`.
- **Falsy** values are treated as `False`.

### The common falsy values

| Falsy value | Description |
|-------------|-------------|
| `False` | The boolean False |
| `0` | The integer zero |
| `0.0` | The float zero |
| `""` | An empty string |

Everything else is **truthy**, such as non-zero numbers and non-empty strings.

Other falsy values you will meet later include `None` and empty collections such as an empty list `[]`.

### Checking with `bool()`

The built-in **`bool()`** function converts a value to its boolean equivalent. It returns `True` for truthy values and `False` for falsy values. It is the easiest way to check how Python sees a value.

```python
print(bool(False))     # False
print(bool(0))         # False
print(bool(''))        # False

print(bool(True))      # True
print(bool(7))         # True
print(bool('Python'))  # True
```

### A few extra cases

```python
print(bool(0.0))       # False
print(bool(None))      # False
print(bool([]))        # False

print(bool(-3))        # True   (any non-zero number is truthy, even negative)
print(bool(' '))       # True   (a string with a space is not empty)
print(bool('0'))       # True   (the text '0' is a non-empty string)
print(bool([0]))       # True   (a list with an item is not empty)
```

Be careful with the last few: `'0'` is truthy because it is a non-empty **string**, even though `0` the number is falsy.

---

## 3. Boolean operators

**Boolean operators**, also called **logical operators**, let you **combine multiple expressions** to build more complex decision-making logic. Python has three:

| Operator | Meaning |
|----------|---------|
| `and` | Both sides must be truthy |
| `or` | At least one side must be truthy |
| `not` | Inverts a value |

---

## 4. The `and` operator

`and` takes two operands. It returns the **first operand if it is falsy**; otherwise, it returns the **second operand**. For the whole expression to be truthy, **both operands must be truthy**.

```python
is_registered = True
age = 30

print(is_registered and age)    # 30
```

It prints `30` because the first operand (`True`) is truthy, so Python moves on and returns the second operand.

More examples showing which operand is returned:

```python
print(0 and 5)        # 0      (first operand is falsy, so it is returned)
print('' and 'x')     # (an empty string is returned, so nothing visible is printed)
print(False and 7)    # False
print(3 and 0)        # 0      (first is truthy, so the second is returned)
```

Notice that `and` does **not always return `True` or `False`**. It returns one of the actual operands.

### Using `and` in an `if` statement

The most common use is to check that **several conditions are all met**. Here is the earlier nested example rewritten with `and`:

```python
is_registered = True
age = 30

if is_registered and age >= 21:
    print('You can enter the event')    # You can enter the event
else:
    print('Entry denied')
```

Both `is_registered` and `age >= 21` are true, so the whole condition is true and the `if` block runs. This is shorter and much easier to read than nested `if` statements.

---

## 5. The `or` operator

`or` returns the **first operand if it is truthy**; otherwise, it returns the **second operand**. The expression is truthy if **at least one operand is truthy**.

```python
score = 45
has_bonus = False

print(score or has_bonus)    # 45
```

It prints `45` because the first operand is truthy, so Python returns it without looking at the second.

More examples:

```python
print(0 or 'default')    # default
print('' or 'guest')     # guest
print(0 or 0.0)          # 0.0   (both falsy, so the second is returned)
```

The `or` operator is often used to provide a **default value** when something is empty, like `'' or 'guest'`.

### Using `or` in an `if` statement

Use `or` to check whether **at least one** condition is true:

```python
age = 70
is_member = False

if age >= 65 or is_member:
    print('You get a senior discount')    # You get a senior discount
else:
    print('No discount available')
```

Here `is_member` is `False`, but `age >= 65` is `True`. Since at least one condition is true, the whole `or` expression is true.

---

## 6. The `not` operator

`not` takes a **single operand** and **inverts its boolean value**. It converts truthy values to `False` and falsy values to `True`.

Unlike `and` and `or`, **`not` always returns `True` or `False`**.

```python
print(not '')          # True    (empty string is falsy)
print(not 'Python')    # False   (non-empty string is truthy)
print(not 0)           # True    (0 is falsy)
print(not 7)           # False   (7 is truthy)
print(not False)       # True
print(not True)        # False
```

### Using `not` in an `if` statement

`not` is commonly used to check whether a value is **falsy**:

```python
is_staff = False

if not is_staff:
    print('Entry restricted to staff members.')    # Entry restricted to staff members.
else:
    print('Welcome, staff member!')
```

Since `is_staff` is `False`, `not is_staff` is `True`, so the first message is printed.

---

## 7. What is short-circuiting?

`and` and `or` are called **short-circuit operators**. **Short-circuiting** means Python checks the operands **from left to right** and **stops as soon as it knows the final result**. The remaining operands are not even evaluated.

- For `and`: if the **first operand is falsy**, the result is already decided, so Python stops.
- For `or`: if the **first operand is truthy**, the result is already decided, so Python stops.

### Seeing it happen

This small function prints a message each time it is called:

```python
def check():
    print('check was called')
    return True
```

Now try it with the operators:

```python
print(False and check())    # False  (check() is never called)
print(True or check())      # True   (check() is never called)
```

In both lines `check()` is skipped, because the result was already known after the first operand.

```python
print(True and check())     # check was called, then True
print(False or check())     # check was called, then True
```

Here the first operand did not decide the result, so Python had to evaluate `check()` too.

### Why it matters

Short-circuiting makes code **faster** and **safer**. You can put a cheap or protective check first, and the later part only runs when it is needed. (For example, you check that something exists before using it.)

---

## 8. Combining operators and precedence

You can combine `and`, `or` and `not` in one expression. Python evaluates them in this order:

1. `not` first
2. `and` second
3. `or` last

```python
print(True or False and False)      # True
print((True or False) and False)    # False
print(not True or True)             # True
print(not (True or True))           # False
```

In the first line, `False and False` is evaluated first (giving `False`), then `True or False` gives `True`. Adding **parentheses** changes the order, as the second line shows.

When an expression is not obvious, use parentheses to make your intention clear.

### Chained comparisons

Python also lets you write a range check in a natural way:

```python
x = 15

print(10 < x < 20)             # True
print(10 < x and x < 20)       # True   (the same thing, written out)
```

---

## 9. Summary table

| Operator | Returns | Example | Result |
|----------|---------|---------|--------|
| `and` | First operand if falsy, else the second | `30 and 5` | `5` |
| `and` | First operand if falsy, else the second | `0 and 5` | `0` |
| `or` | First operand if truthy, else the second | `45 or False` | `45` |
| `or` | First operand if truthy, else the second | `0 or 'default'` | `default` |
| `not` | Always `True` or `False` | `not 0` | `True` |

| Operator | Short-circuits when |
|----------|---------------------|
| `and` | The first operand is falsy |
| `or` | The first operand is truthy |

---

## 10. Why this matters in cybersecurity

- **Access control**: allow access only if the user is logged in `and` has the right role.
- **Multiple checks**: block a request if the IP is blacklisted `or` the rate limit is exceeded.
- **Validating input**: use `not` to reject empty values (an empty string is falsy).
- **Default values**: use `or` to fall back to a default setting when none is given.
- **Safe checks**: use short-circuiting to check that a value exists before using it.

---

## 11. Common mistakes

- Thinking `and` and `or` always return `True` or `False`. They return one of the **operands**.
- Forgetting that the string `'0'` and the string `'False'` are **truthy**, because they are non-empty strings.
- Writing `if x == 1 or 2:`, which is always truthy because `2` on its own is truthy. Write `if x == 1 or x == 2:`.
- Mixing up `and` and `or` when combining conditions.
- Relying on the order of evaluation without **parentheses** when the expression is complex.
- Writing deeply **nested** `if` statements when `and` would be clearer.