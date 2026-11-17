# Strings, Multiline strings, 'in' operator

Lecture "What Are Strings?". 

---

## 1. What is a string?

A string is a **sequence of characters surrounded by quotation marks**. Python accepts either **single quotes** (`'...'`) or **double quotes** (`"..."`), and both create exactly the same kind of value. Use whichever you prefer, but stay consistent in a project.

```python
city = 'Lahore'
country = "Pakistan"
```

Strings are used for almost any text: usernames, IP addresses, file paths, URLs, passwords and messages. In cybersecurity scripts you will work with strings constantly.

Remember that anything inside quotes is a string, even if it looks like a number. `"443"` is text, not an integer.

---

## 2. Multiline strings

A normal string must fit on one line. For text that spans several lines, use **triple quotes**: either three double quotes or three single quotes. Everything between them, including line breaks, becomes part of the string.

```python
note = """Line one
Line two"""

note2 = '''First
Second
Third'''
```

Printing `note` shows:

```
Line one
Line two
```

Triple quotes are handy for long messages, banners and descriptions.

---

## 3. Quotes inside a string

What if the text itself contains a quotation mark? A string would end early, so there are two solutions.

### Option 1: use the opposite kind of quotes

If the text contains single quotes, wrap the string in double quotes, and the other way around.

```python
msg = "It's a rainy day"
quote = 'He said, "Good morning!"'
```

### Option 2: escape the quote with a backslash

A backslash (`\`) before the quote tells Python "treat this as a normal character, not the end of the string". This works with either kind of outer quotes.

```python
msg = 'It\'s a rainy day'
quote = "He said, \"Good morning!\""
```

Both options give the same result:

```
It's a rainy day
He said, "Good morning!"
```

Option 1 is usually cleaner. Use option 2 when the text contains both kinds of quotes.

---

## 4. Escape sequences

The backslash can also combine with a character to produce something that is **hard to type directly** inside a string. These combinations are called **escape sequences**.

| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\t` | Tab (a wide space) |
| `\\` | A single backslash |

```python
print('Good\nmorning')
print('City:\tLahore')
print('D:\\Projects\\Python')
```

Output:

```
Good
morning
City:	Lahore
D:\Projects\Python
```

- `\n` moves the following text to a new line.
- `\t` adds a tab between `City:` and `Lahore`.
- `\\` is needed because a single backslash starts an escape sequence, so to print a real backslash you write it twice. This matters a lot for **Windows file paths**.

---

## 5. Checking for characters with `in`

The `in` operator checks whether a character or a group of characters exists inside a string. It returns a **boolean** (`True` or `False`).

```python
text = 'Python is fun'

print('Python' in text)   # True
print('java' in text)     # False
print('is' in text)       # True
print('y' in text)        # True
print('z' in text)        # False
```

Important points:

- It works for a single character or for a longer piece of text (a **substring**).
- It is **case-sensitive**: `'python' in text` would be `False` because the text has a capital `P`.
- The pieces must appear together in that exact order, so it checks for a whole substring, not separate letters.

In security work, `in` is often used to search for a keyword inside a log line or a web response.

---

## 6. Common mistakes

- Starting with a quote and forgetting to close it (`SyntaxError`).
- Mixing quote types incorrectly, for example `'It's a day'`, where the apostrophe ends the string early.

