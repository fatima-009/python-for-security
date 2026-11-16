# Declaring Variables in Python

This file focuses on understanding the ideas, with only short examples.

---

## 1. What does "declaring" a variable mean?

In many languages (C, Java and others), you must **declare** a variable first by announcing its name and type, and only then give it a value.

Python is different. **There is no separate declaration step.** A variable comes into existence the moment you first assign a value to it. Declaring and initializing (giving the first value) happen together in one line.

```python
username = "admin"
```

This single line creates the name `username`, stores the text `"admin"` in memory, and connects the name to that value.

### How it works behind the scenes

A Python variable is not really a box that holds a value. It is better to think of it as a **name tag attached to a value**. The value lives in memory, and the variable is just a label pointing to it. This is why:

- You can move the label to a different value at any time (reassignment).
- Two names can point to the same value.
- The label itself has no type. The **value** has the type.

---

## 2. Declaring with an initial value

The basic pattern is:

```
variable_name = value
```

Key points:

- The **name** is on the left, the **value** on the right.
- The `=` sign is the **assignment operator**. It means "store this value under this name", not "is equal to".
- Python evaluates the right side first, then attaches the name to the result. So `total = 5 + 3` first calculates `8`, then stores it in `total`.
- A variable must be given a value when it is created. You cannot create an "empty" variable with no value at all.

### Using a variable before declaring it

If you use a name that has never been assigned, Python raises a `NameError`. This is one of the most common beginner errors. It usually means the name was misspelled, written with the wrong capitalization, or used before the line that creates it.

---

## 3. Dynamic typing

You never write the type when declaring. Python looks at the value and decides the type by itself. This is called **dynamic typing**.

```python
data = 10          # an int
data = "hello"     # now a str
```

The same name can point to a different type later without any error. This is flexible and quick, but it also means you should keep track of what a variable is meant to hold, otherwise bugs can slip in. Use `type()` to check when unsure.

---

## 4. Declaring a variable with no real value yet

Sometimes you need a variable to exist but do not have its real value yet. The usual approach is to give it the special value `None`, which means "no value".

```python
result = None
```

This is a clear way of saying "this will be filled in later". Another common approach is to use a neutral starting value, like `0` for a counter or `""` for empty text.

---

## 5. Declaring several variables

### Multiple variables, multiple values (one line)

```python
ip_address, port = "10.0.0.5", 80
```

The values are matched to the names **in order**. The number of names must equal the number of values, otherwise Python raises a `ValueError`.

### Multiple variables, one value (chained assignment)

```python
a = b = c = 0
```

All three names point to the same value. This is fine for simple values like numbers and text.

### Unpacking

Values stored in a collection, such as a list or tuple, can be split into separate variables in one step.

```python
host, port = ("example.com", 443)
```

This is called **unpacking** and you will use it often later.

### Swapping two variables

Python lets you swap values without a temporary third variable:

```python
a, b = b, a
```

---

## 6. Changing a variable after declaring it

### Reassignment

Assigning again with the same name simply moves the label to the new value. The old value is forgotten if nothing else uses it.

### Updating based on the current value

A very common pattern is to calculate a new value from the old one. Python has shorthand operators for this:

    | Shorthand |   Same as   |
    | `x += 1`  | `x = x + 1` |
    | `x -= 1`  | `x = x - 1` |
    | `x *= 2`  | `x = x * 2` |
    | `x /= 2`  | `x = x / 2` |

These are handy for counters, such as counting failed login attempts.

### Deleting a variable

The `del` keyword removes a name. After that, using it causes a `NameError`.

```python
del username
```

This is rarely needed in everyday code, but it is good to know it exists.

---

## 7. Constants

Python has **no true constants**. Nothing stops you from changing any variable. The community convention is to write the names of values that should not change in **UPPER_CASE**.

```python
MAX_ATTEMPTS = 5
```

This is a message to other programmers (and your future self): "do not change this". Python itself will not enforce it.

---

## 8. Type hints (optional)

Although Python does not require types, you can add an optional **type hint** to show what you expect a variable to hold:

```python
port: int = 443
```

Important points:

- Type hints are **documentation only**. Python does not stop you from assigning a different type.
- They make code easier to read, and editors like VS Code use them to give helpful warnings.
- Beginners can safely ignore them at first. You will see them often in professional code.

---

## 9. Where a variable is visible (scope, a short preview)

A variable's **scope** is the part of the program where it can be used.

- A variable created outside any function is **global** and can be used almost everywhere in the file.
- A variable created inside a function is **local** and exists only inside that function.

Scope is covered properly when you learn functions. For now, just know that a variable is not always available everywhere.

---

## 10. Good habits when declaring variables

- Choose **clear, descriptive names** in `snake_case`.
- Declare a variable **close to where it is first used**, not far above.
- **Give meaningful starting values** instead of leaving things unclear.
- Do not reuse one name for unrelated things. It confuses both you and the reader.
- Never use built-in names such as `print`, `type` or `list` as variable names. Python allows it, but it overwrites the built-in function and breaks your code in confusing ways.

---

## 11. Common mistakes

- Using a variable before assigning it (`NameError`).
- Misspelling a name or changing its capitalization.
- Mixing up the number of names and values in a multiple assignment.
- Using `=` when you meant to compare. Comparison uses `==` and is covered later.
- Accidentally overwriting a built-in function name.
- Starting a name with a number or using spaces or hyphens.

---

## 12. Key takeaways

- Python has no separate declaration step. Assigning a value creates the variable.
- The `=` operator stores the value on the right under the name on the left.
- A variable is a name tag pointing to a value, and the type belongs to the value.
- Typing is dynamic, so the same name can later point to a different type.
- Use `None` for "no value yet", unpack to declare several variables at once, and use UPPER_CASE for constants by convention.
- Type hints are optional documentation, not enforced rules.
