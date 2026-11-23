# Conditional Statements and Comparison Operators


## 1. What are conditional statements?

**Conditional statements**, or **conditionals**, let you control the **flow of your program** based on whether certain conditions are true or false. Instead of running every line from top to bottom, the program can **make decisions**.

Before using conditionals, you need their basic building blocks: **comparison operators**.

---

## 2. Comparison operators

Comparison operators let you **compare two or more values** and they **return a boolean value**. Remember that a boolean can only be `True` or `False`.

| Operator | Name | Description |
|----------|------|-------------|
| `==` | Equal | Checks if two values are equal |
| `!=` | Not equal | Checks if two values are not equal |
| `>` | Greater than | Checks if the left value is greater than the right value |
| `<` | Less than | Checks if the left value is less than the right value |
| `>=` | Greater than or equal | Checks if the left value is greater than or equal to the right value |
| `<=` | Less than or equal | Checks if the left value is less than or equal to the right value |

### Expressions that evaluate to True or False

```python
print(12 > 7)     # True
print(12 < 7)     # False
print(12 == 7)    # False
print(7 == 7)     # True
print(12 != 7)    # True
print(12 >= 7)    # True
print(12 <= 7)    # False
```

### Things to notice

- `>=` and `<=` are `True` when the values are **equal** as well:

```python
print(7 >= 7)     # True
print(7 <= 7)     # True
```

- Comparison operators also work with **strings**, and string comparison is **case-sensitive**:

```python
print('a' == 'a')    # True
print('a' == 'A')    # False
```

- Values of different types can be compared too. An integer and a float with the same value are equal, but a **string is never equal to a number**:

```python
print(5 == 5.0)      # True
print('5' == 5)      # False
```

### `=` versus `==`

This is a very common mistake.

- `=` is the **assignment** operator: it stores a value in a variable.
- `==` is the **comparison** operator: it checks whether two values are equal.

Using `=` where a comparison is needed is an error:

```python
x = 5
if x = 5:
    pass
```

```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

(The exact wording of this message can differ between Python versions.)

---

## 3. The `if` statement

The comparison operators can be used in conditionals to run certain code **only when a condition is true**. The most basic conditional is the **`if` statement**.

### Syntax

```python
if condition:
    pass    # Code to execute if condition is True
```

- An `if` statement starts with the **`if` keyword**.
- `condition` is an **expression** followed by a **colon** (`:`).
- The body of the `if` statement is a **code block**: a group of statements that belong together.

### Indentation

Spaces at the beginning of a line are called **indentation**. In Python, **indentation decides which statements belong to a code block**. Other languages use curly braces for this, but Python uses indentation.

The Python style guide recommends **four spaces** for each level. You may use any number of spaces as long as you are **consistent**.

### Example

```python
age = 21

if age >= 18:
    print('You are old enough to vote')    # You are old enough to vote
```

The four spaces before `print(...)` place that line **inside** the `if` block. The code inside the block runs **only when the condition is true**.

If the condition is false, nothing in the block runs, and nothing is printed:

```python
age = 15

if age >= 18:
    print('You are old enough to vote')    # Nothing shows up in the terminal
```

### Code after the block

Lines that are **not indented** are outside the block, so they always run:

```python
age = 15

if age >= 18:
    print('You are old enough to vote')
print('after')    # after (this always runs)
```

### The `pass` statement

The body of an `if` statement cannot be empty. The **`pass`** statement does nothing when executed. It is a **placeholder** for code you will write later, and it is useful wherever an empty block is not allowed.

```python
if age >= 18:
    pass    # I will write this part later
```

### `IndentationError`

If the line after the `if` is not indented, Python raises an **`IndentationError`**. This is how Python signals that indentation is required.

```python
age = 20

if age >= 18:
print('You are old enough to vote')
```

```
IndentationError: expected an indented block after 'if' statement on line 3
```

Blocks are also found in **loops and functions**, which you will learn about in future lessons.

---

## 4. The `else` clause

What if you also want something to happen when the condition is **false**? That is what the **`else` clause** is for. It runs when the `if` condition is false.

### Syntax

```python
if condition:
    pass    # Code to execute if condition is True
else:
    pass    # Code to execute if condition is False
```

### Example

```python
marks = 40

if marks >= 50:
    print('You passed')
else:
    print('You failed')    # You failed
```

Exactly **one** of the two blocks runs, never both and never neither.

### Nothing between `if` and `else`

You **cannot place any statements between** the `if` block and the `else` clause. This raises a `SyntaxError`:

```python
age = 12

if age >= 18:
    print('You are old enough to vote')
print('Almost there!')
else:
    print('You are not old enough yet')
```

```
SyntaxError: invalid syntax
```

The `print('Almost there!')` line is not indented, so it ends the `if` statement. The `else` then has no `if` to belong to.

---

## 5. The `elif` clause

Sometimes you need to check **several conditions**. Python lets you extend an `if` statement with **`elif`** (short for "else if").

### Syntax

```python
if condition1:
    pass    # Runs if condition1 is True
elif condition2:
    pass    # Runs if condition1 is False and condition2 is True
else:
    pass    # Runs if all conditions are False
```

### Example

```python
marks = 64

if marks >= 80:
    print('Excellent')
elif marks >= 50:
    print('Passed')    # Passed
else:
    print('Failed')
```

Here `64 >= 80` is false, so Python moves on to the `elif`. `64 >= 50` is true, so it prints `Passed` and skips the rest.

### As many `elif` clauses as you like

```python
temperature = -3

if temperature >= 35:
    print('Very hot')
elif temperature >= 25:
    print('Warm')
elif temperature >= 15:
    print('Mild')
elif temperature >= 5:
    print('Cool')
else:
    print('Freezing')    # Freezing
```

### Only the first true branch runs

Python checks the conditions **from top to bottom** and runs **only the first block whose condition is true**. After that, it skips all the remaining `elif` and `else` parts, even if they would also be true.

This means the **order matters**. With `marks = 85`:

```python
marks = 85

if marks >= 80:
    print('Excellent')    # Excellent (the elif is never checked)
elif marks >= 50:
    print('Passed')
```

If you put the `>= 50` check first, `85` would match it and print `Passed` instead. Always put the **most specific** condition first.

### `else` is optional

`if` can be used alone, with `else`, with `elif`, or with all three. The `else` clause, when present, always comes **last**.

---

## 6. Summary of the structure

| Part | Needed? | Runs when |
|------|---------|-----------|
| `if` | Required, always first | Its condition is true |
| `elif` | Optional, as many as needed | Earlier conditions were false and its own is true |
| `else` | Optional, always last | All the earlier conditions were false |

Every `if`, `elif` and `else` line ends with a **colon**, and its block is **indented**.

---

## 7. Why this matters in cybersecurity

- **Checking a login**: if the password matches, allow access, else deny.
- **Limiting attempts**: if failed attempts reach a limit, lock the account.
- **Classifying severity**: use `elif` to label an event as low, medium, high or critical.
- **Checking a port's state**: if open, report it, else skip it.
- Deciding what a script does based on **input** or **results**.
