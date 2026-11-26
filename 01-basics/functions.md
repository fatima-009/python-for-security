# Functions in Python

## 1. What are functions?

**Functions are reusable pieces of code that run when you call them.** Instead of writing the same instructions again and again, you write them once, give them a name, and run them whenever you need.

You have already used **built-in functions**, which Python provides for you, such as `print()`, `len()`, `type()` and `round()`.

### The `input()` function

`input()` is a built-in function that **prompts the user to type something**. It shows the text you give it, waits for the user to type and press Enter, and **returns what they typed**.

```python
name = input('What is your name? ')    # User types "Zain" and presses Enter
print('Hello', name)                   # Output: Hello Zain
```

Important: `input()` **always returns a string**, even if the user types digits.

```python
print(type(name))                      # <class 'str'>

age_text = input('Your age? ')         # User types 27
print(type(age_text))                  # <class 'str'>
print(type(int(age_text)))             # <class 'int'>
```

To use the typed value as a number, convert it with `int()` (or `float()`).

### The `int()` function

`int()` converts a number, a boolean, or a string that represents an integer into an **integer**.

```python
print(int(7.99))     # 7     (the decimal part is cut off, not rounded)
print(int('85'))     # 85
print(int(True))     # 1
print(int(False))    # 0
print(int(-2.7))     # -2    (it cuts toward zero)
```

---

## 2. Defining and calling functions

You can also write your own **custom functions**.

### Defining a function

Use the **`def`** keyword, followed by:

1. The **name** you want to give the function.
2. A pair of **parentheses** `()`.
3. A **colon** `:`.

Then, on a new line, write the code the function should run, **indented**. The code the function runs is called the function's **body**.

```python
def hello():
    print('Good Morning')
```

Defining a function does **not run it**. It only saves the instructions under that name.

### Calling a function

To run the function, **call** it by writing its name followed by a pair of parentheses:

```python
hello()     # Good Morning
```

You can call the same function as many times as you like. Each call runs the whole body again.

### Indentation and code blocks

Notice the indentation before `print('Good Morning')`. Python relies on indentation to decide which statements belong together. These groups of statements are called **code blocks**. The function body is a code block, and it ends when the indentation goes back to the left.

---

## 3. Parameters and arguments

Here is a function that prints the sum of two numbers:

```python
def calculate_sum(a, b):
    print(a + b)
```

### Parameters

`a` and `b` inside the parentheses are called **parameters**. Think of them as **placeholder variables** or "slots" for the values you pass into the function when you call it. Multiple parameters are separated by commas.

### Arguments

To use the parameters, you pass in **arguments**. Arguments are the **actual values** you give to a function when you call it.

```python
calculate_sum(8, 5)     # 13
```

| Term | Where | Example |
|------|-------|---------|
| Parameter | In the function **definition** | `a` and `b` in `def calculate_sum(a, b):` |
| Argument | In the function **call** | `8` and `5` in `calculate_sum(8, 5)` |

### The wrong number of arguments

If you call the function with the wrong number of arguments, Python raises a `TypeError`.

```python
calculate_sum()
# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'

calculate_sum(8)
# TypeError: calculate_sum() missing 1 required positional argument: 'b'

calculate_sum(8, 5, 2)
# TypeError: calculate_sum() takes 2 positional arguments but 3 were given
```

---

## 4. Positional and keyword arguments

### Positional arguments

The arguments in `calculate_sum(8, 5)` are **positional arguments**. Python matches them to the parameters **by position**: `8` goes to `a` and `5` goes to `b`.

Here is a function where the **order matters**:

```python
def introduce(name, age):
    print(f'My name is {name} and I am {age} years old.')

introduce('Hamza', 30)
# My name is Hamza and I am 30 years old.
```

If you swap the positional arguments, each value lands in the wrong parameter:

```python
introduce(30, 'Hamza')
# My name is 30 and I am Hamza years old.
```

Python does not complain, because it cannot know which value you meant. The result is simply wrong.

### Keyword arguments

You can also pass **keyword arguments**: write the parameter name, then `=`, then the value. Python matches these **by name**, so the order no longer matters.

```python
introduce(age=30, name='Hamza')
# My name is Hamza and I am 30 years old.
```

Here, `name='Hamza'` passes `'Hamza'` to the `name` **parameter**. It does **not** create a variable named `name` outside the function.

### Mixing positional and keyword arguments

You can combine both kinds, but the **positional arguments must come first**:

```python
introduce('Hamza', age=30)
# My name is Hamza and I am 30 years old.
```

### Argument mistakes

**A positional argument after a keyword argument** causes a `SyntaxError`:

```python
introduce(name='Hamza', 30)
# SyntaxError: positional argument follows keyword argument
```

**The same parameter given more than once** causes a `TypeError`:

```python
introduce('Hamza', name='Bilal', age=30)
# TypeError: introduce() got multiple values for argument 'name'
```

Here, the positional argument `'Hamza'` already supplies the value for `name`, so `name='Bilal'` is a second value for the same parameter.

**A keyword that does not match any parameter** is also an error:

```python
introduce('Hamza', city='Lahore')
# TypeError: introduce() got an unexpected keyword argument 'city'
```

---

## 5. Returning values from functions

Functions use the special **`return`** keyword to **exit the function and send a value back** to the place where the function was called.

### Without `return`

If you do not explicitly use `return`, Python returns **`None`** by default. As you learned in the identity operators lesson, `None` represents the **absence of a value**. Here it means the function has not returned an explicit result.

```python
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(8, 5)    # 13
print(my_sum)                   # None
```

The function **prints** the sum, but it does not **return** it. So when its result is stored in `my_sum`, the value is `None`.

### With `return`

Use `return` to send the result back:

```python
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(8, 5)
print(my_sum)                   # 13
```

Now the function returns the sum, and it gets stored in `my_sum`.

### Printing vs returning

| | `print()` inside the function | `return` |
|---|-------------------------------|----------|
| What it does | Shows the value on the screen | Sends the value back to the caller |
| Can the value be reused? | No | Yes, store it or use it in another expression |
| Value of the call | `None` | The returned value |

Because a returned value can be reused, you can pass the result of one call into another:

```python
print(calculate_sum(calculate_sum(1, 2), 4))    # 7
```

### `return` ends the function immediately

Any code after a `return` statement in the same block is **never executed**:

```python
def early(x):
    return x * 2
    print('never printed')

print(early(4))    # 8
```

### A function that does nothing

A function with no `return` and an empty body is not allowed. Use the `pass` statement as a placeholder. Calling it gives `None`:

```python
def nothing():
    pass

print(nothing())    # None
```

---

## 6. Summary table

| Concept | Meaning | Example |
|---------|---------|---------|
| Function | A reusable block of code | `def hello():` |
| Body | The indented code the function runs | `print('Good Morning')` |
| Call | Running the function | `hello()` |
| Parameter | A placeholder in the definition | `a`, `b` |
| Argument | A value passed in the call | `8`, `5` |
| Positional argument | Matched by position | `introduce('Hamza', 30)` |
| Keyword argument | Matched by name | `introduce(age=30, name='Hamza')` |
| `return` | Sends a value back and exits | `return a + b` |
| Default return value | `None` when there is no `return` | |

---

## 7. Why this matters in cybersecurity

- **Reusing code**: write a port-checking or hash-checking function once and use it for many targets.
- **Organizing scripts** into small named pieces that are easier to test and fix.
- **Returning results**, such as `True` or `False` for a check, so other code can make decisions.
- **Keyword arguments** make calls readable, such as `scan(host='10.0.0.5', port=22)`.
- Almost every security tool and library is built from functions.

---

## 8. Common mistakes

- Defining a function but **forgetting to call it**. Nothing happens until you call it.
- Forgetting the **parentheses** when calling (`hello` is not the same as `hello()`).
- Forgetting the **colon** after the parentheses in the definition.
- Forgetting to **indent** the function body.
- Passing the **wrong number** of arguments (`TypeError`).
- Mixing up the **order** of positional arguments.
- Putting a positional argument **after** a keyword argument.
- Using `print()` when you actually need `return`, then getting `None`.
- Writing code **after** `return` and expecting it to run.
- Forgetting that `input()` returns a **string**.