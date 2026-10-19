# Variables, Naming Conventions and print()

This file focuses on understanding the ideas, with only a few short examples.


## 1. What is a variable?

A variable is a **name that points to a value stored in the computer's memory**. Think of it as a labeled box: the label is the variable's name and whatever is inside the box is its value.

Programs constantly need to remember information, such as a username, a number of login attempts, or an IP address. Variables are how a program does that. Without them, every value would have to be typed again and again, and nothing could change while the program runs.

### Creating a variable

A variable is created the moment you give it a value. This is called **assignment**, and it uses the `=` sign.

```python
username = "admin"
login_attempts = 3
```

Important points:

- The `=` sign here does **not** mean "equal to" like in maths. It means "store the value on the right into the name on the left".
- The name goes on the **left**, the value on the **right**.
- Python has no special keyword for creating a variable (unlike some languages that need `var` or `int`). Assignment alone is enough.

### Variables can change

The word "variable" means the value can vary. You can give the same name a new value whenever you like, and the old value is replaced.

```python
login_attempts = 3
login_attempts = 4   # now the value is 4
```

### Python figures out the type itself

In Python you do not have to say what kind of data a variable will hold. Python looks at the value and decides. This is called **dynamic typing**. It makes code shorter and easier to write, though it also means you must be careful not to mix up types by accident (more on types in the next topic).

### Why variables matter in cybersecurity

In security scripts, variables will hold things like a target IP address, a port number, a file path, a password hash, or the number of failed logins. Clear variables make scripts easier to read and fix.


## 2. Naming conventions

Choosing a name for a variable has two layers: **rules** that Python forces you to follow, and **conventions** that the Python community recommends.

### Rules (breaking these causes an error)

1. A name can contain only **letters, numbers and underscores** (`_`).
2. A name **cannot start with a number**. `user1` is fine, `1user` is not.
3. **No spaces or special characters** such as `-`, `@`, `$` or `!`.
4. Names are **case-sensitive**. `name`, `Name` and `NAME` are three different variables.
5. You cannot use **reserved keywords**. Words like `if`, `for`, `while`, `class` and `True` already have a meaning in Python.

### Conventions (not forced, but good practice)

These come from PEP 8, Python's official style guide.

- **Use snake_case.** Write names in lowercase and separate words with underscores: `failed_logins`, `target_ip`.

- **Use descriptive names.** A reader should understand what a variable holds without hunting through the code. `failed_logins` is much clearer   
than `fl` or `x`.

- **Use UPPER_CASE for constants.** If a value should never change while the program runs, write its name in capitals: `MAX_ATTEMPTS`. Python will not stop you from changing it, but the capitals signal "leave this alone".

- **Avoid confusing single letters** such as `l`, `O` and `I`, which look like the numbers `1` and `0`.

- **Keep names reasonably short.** Descriptive does not mean a whole sentence.

### Good and bad examples

|   Bad name  |         Why it is bad          |          Better name           |

| `x`         | Says nothing about the content | `port_number`                  |
| `UserName`  | Not snake_case                 | `user_name`                    |
| `2fa_code`  | Starts with a number           | `fa_code` or `two_factor_code` |
| `user-name` | Hyphen not allowed             | `user_name`                    |

---

## 3. The print() function

### What it does

`print()` is a **built-in function** that displays output on the screen. It is the simplest way to see what your program is doing, and it is also very useful for **debugging**: if something is not working, print the variable and check its value.

A function is a reusable piece of code with a name. You use ("call") it by writing its name followed by parentheses. Whatever you want to show goes inside the parentheses.

```python
print("Hello, world!")
```

### What can be printed

- **Text (strings)**: must be inside quotes, single or double. `print("hello")`
- **Numbers**: no quotes needed. `print(100)`
- **Variables**: write the name without quotes and Python prints the value stored in it.

A common beginner mistake is mixing these up. `print(username)` shows the value inside the variable, while `print("username")` simply shows the word *username*.

### Printing more than one thing

You can pass several items separated by commas. Python places a space between them.

```python
print("User:", username, "Attempts:", login_attempts)
```

### Optional settings

`print()` has options that change how the output looks:

- **`sep`** controls the separator between items (a space by default).
- **`end`** controls what is printed at the very end (a new line by default). Changing it lets the next print continue on the same line.

```python
print("192", "168", "1", "1", sep=".")   # 192.168.1.1
```

### f-strings

An f-string lets you put variables directly inside a sentence. Place an `f` before the opening quote and wrap variable names in curly braces. This is usually cleaner than using commas.

```python
print(f"User {username} has {login_attempts} attempts")
```

### Escape characters

Some characters have a special job inside text. They start with a backslash:

| Code |              Meaning             |

| `\n` | New line                         |
| `\t` | Tab (a wide space)               |
| `\"` | A quotation mark inside a string |
| `\\` | A backslash                      |


## 4. Common mistakes

- Using `=` when you meant to compare values (comparing comes later and uses `==`).
- Forgetting quotes around text, which makes Python think it is a variable name.
- Writing a variable name with different capitalization than when it was created.
- Using a variable before giving it a value, which causes a `NameError`.
- Using a keyword as a variable name.


## 5. Key takeaways

- A variable is a named place to store a value, and its value can change.
- Create one with `=`, name on the left and value on the right.
- Follow the naming rules, and use clear `snake_case` names for readable code.
- `print()` displays values and is the easiest way to check what your program is doing.
- f-strings are a neat way to combine text and variables in output.


## Practice ideas

1. Create variables for your name, age and favorite programming language, then print them in one sentence.
2. Change one variable's value and print it again to see the difference.
3. Try creating a variable with an invalid name on purpose and read the error message Python gives.