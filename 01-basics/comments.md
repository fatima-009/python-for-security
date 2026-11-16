# Comments in Python (#)

This file focuses on understanding the ideas, with only short examples.

---

## 1. What is a comment?

A comment is a piece of text inside your code that **Python completely ignores**. It is not executed and has no effect on how the program runs. Comments exist only for **humans**: the people who read the code, including you a few weeks from now.

In Python, a comment starts with the **hash symbol `#`**. Everything from the `#` to the end of that line is the comment.

```python
# This is a comment
print("Hello")
```

Only the `print()` line runs. The first line is skipped.

---

## 2. Why use comments?

- **Explain why** the code does something, not just what it does.
- **Make code easier to understand** when you come back to it later.
- **Help other people** (teammates, or people reading your GitHub repo) follow your thinking.
- **Organize code** into sections with headings.
- **Leave reminders** about things to fix or improve later.
- **Temporarily disable code** without deleting it, which is useful when testing and debugging.

In cybersecurity, scripts are often shared, reviewed and reused, so clear comments are especially valuable. A short note explaining why a certain port or timeout was chosen can save a lot of confusion.

---

## 3. Types of comments

### Full-line comment

The whole line is a comment. This is the most common type.

```python
# Set the number of allowed login attempts
max_attempts = 3
```

### Inline comment

A comment placed **after code on the same line**. Leave at least two spaces between the code and the `#`, and one space after the `#`, as recommended by PEP 8.

```python
port = 443  # default HTTPS port
```

Use inline comments sparingly. They are best for short clarifications.

### Multi-line comments

Python has **no special multi-line comment symbol** (unlike `/* ... */` in some languages). There are two ways to write comments over several lines.

**Option 1: several `#` lines.** This is the preferred and most common way.

```python
# This script checks whether a port is open.
# It only works on systems I own or on lab machines.
# Results are printed at the end.
```

**Option 2: a triple-quoted string.** Text inside `""" ... """` that is not assigned to anything is ignored in practice, so some people use it like a comment. Technically it is a string, not a comment, so use it mainly for **docstrings** (see below) rather than as a general replacement for `#`.

### Docstrings (a special kind of documentation)

A **docstring** is a triple-quoted string placed at the very start of a file, function or class. It describes what that piece of code does. Unlike a normal comment, Python **stores** it, and tools can read it. You will use docstrings properly when you learn functions.

```python
"""
variables.py
Notes and practice for variables.
"""
```

---

## 4. Using comments to disable code

Putting `#` in front of a line stops it from running, without deleting it. This is called **commenting out** code.

```python
print("This runs")
# print("This does not run")
```

This is helpful while debugging: you can switch lines off and on to find a problem. In VS Code, select the lines and press **`Ctrl + /`** to comment or uncomment them all at once.

Do not leave large amounts of commented-out code in your finished work, though. It makes files messy. If you use Git, old code is saved in history anyway.

---

## 5. Where a `#` is not a comment

If `#` appears **inside a string** (inside quotes), it is just a normal character and not a comment.

```python
print("Item #1")    # prints: Item #1
```

Python only treats `#` as a comment when it is outside of quotes.

---

## 6. Writing good comments

### Do

- Explain the **reason** behind the code ("why"), not what is obvious ("what").
- Keep comments **short and clear**.
- **Update comments** when you change the code. A wrong comment is worse than none.
- Use proper spelling and a consistent style.
- Add a short comment above a block of code that does one job.
- Put a **header comment** at the top of a file saying what it is for.

### Don't

- Don't repeat the code in words.
- Don't comment every single line. Good, clear names reduce the need for comments.
- Don't write comments that contradict the code.
- Don't use comments to excuse confusing code. Rewrite the code to be clearer instead.
- Never put passwords, API keys or other secrets in comments, especially in files you upload to GitHub. Comments are fully visible to anyone who sees the file.

### Bad vs good example

    |      Bad comment      |    Why it is weak     |                     Better comment                     |
    | `x = 5  # set x to 5` | Just repeats the code | `retries = 5  # server drops connection after 5 tries` |
    | `# loop`              | Says nothing useful   | `# check each port in the scan range`                  |

---

## 6.1 Special comments you may see

- **TODO**: a reminder of work still to be done, for example `# TODO: add input validation`.
- **FIXME**: marks something known to be broken.
- **Shebang line**: `#!/usr/bin/env python3` at the very top of a script tells Linux which interpreter to use. It looks like a comment (and Python treats it as one), but the operating system reads it. You will see it in many security scripts.

---

## 7. Common mistakes

- Forgetting the `#`, so Python tries to run the text and gives a `SyntaxError`.
- Putting the `#` in the wrong place and commenting out code you wanted to keep.
- Assuming triple quotes are a perfect multi-line comment.
- Leaving outdated comments after changing the code.
- Leaving secrets in comments.

