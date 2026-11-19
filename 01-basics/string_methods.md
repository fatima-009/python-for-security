# Common String Methods


## 1. What is a method?

A **method** is a function that you call **on a value**. To call a string method, write the string (or the variable that holds it), then a **dot**, then the method name with parentheses.

```python
text = 'good morning pakistan'
text.upper()
```

Methods are closely tied to the type of value they belong to. String methods work on strings, list methods work on lists, and so on. You will learn more about how methods work when you study classes and objects later.

### One rule to remember

Strings are **immutable**, so a string method **never changes the original string**. It returns a **new** value. If you want to keep the result, store it in a variable.

```python
shout = text.upper()
print(shout)    # GOOD MORNING PAKISTAN
print(text)     # good morning pakistan  (unchanged)
```

All the examples below use this string unless stated otherwise:

```python
s = 'good morning pakistan'
```

---

## 2. Changing case

### `upper()`

Returns a new string with **all characters in uppercase**.

```python
print(s.upper())    # GOOD MORNING PAKISTAN
```

### `lower()`

Returns a new string with **all characters in lowercase**.

```python
print('Good Morning Pakistan'.lower())   # good morning pakistan
```

### `capitalize()`

Returns a new string with the **first character capitalized** and **all the other characters lowercased**.

```python
print('pYTHON rocks'.capitalize())       # Python rocks
```

Only the very first character of the whole string is capitalized, not the first letter of every word.

### `title()`

Returns a new string with the **first letter of each word capitalized** and the remaining letters lowercased.

```python
print(s.title())    # Good Morning Pakistan
```

### Why case methods matter

Comparing text is **case-sensitive**: `'Admin'` and `'admin'` are different strings. Converting both to lowercase with `lower()` before comparing is a common way to make checks reliable, for example when matching usernames or keywords.

---

## 3. Checking case: `isupper()` and `islower()`

### `isupper()`

Returns `True` if the string contains **at least one cased character** (a letter) and **all letters are uppercase**. Otherwise it returns `False`.

```python
print('PYTHON'.isupper())    # True
print('Python'.isupper())    # False
```

### `islower()`

Returns `True` if the string contains at least one letter and **all letters are lowercase**. Otherwise it returns `False`.

```python
print('python'.islower())    # True
print('Python'.islower())    # False
```

### A detail worth knowing

A string with **no letters at all** returns `False` for both methods, because there is no cased character to check:

```python
print('12345'.isupper())     # False
```

---

## 4. Removing extra spaces: `strip()`

Returns a new string with **leading and trailing characters removed**. If you pass no argument, it removes **whitespace** (spaces, tabs and newlines) from the start and end.

```python
raw = '   admin   '
print(raw.strip())      # admin
print(repr(raw))        # '   admin   '  (original unchanged)
```

(`repr()` is used here only to show the quotes and spaces clearly.)

You can also pass the characters you want removed from both ends:

```python
print('xxhelloxx'.strip('x'))    # hello
```

Note that `strip()` only removes characters at the **start and end**, never in the middle. It is very useful for cleaning text that comes from files or user input.

---

## 5. Replacing text: `replace(old, new)`

Returns a new string in which **all occurrences** of `old` are replaced by `new`.

```python
print(s.replace('morning', 'evening'))    # good evening pakistan
print(s.replace('o', '0'))                # g00d m0rning pakistan
```

It replaces **every** match, not only the first one. If `old` is not found, you simply get the same text back.

---

## 6. Splitting and joining

### `split(separator)`

**Splits** a string on a separator and returns a **list** of strings. (A list groups values between square brackets.) If no separator is given, `split()` splits on **whitespace**.

```python
print(s.split())             # ['good', 'morning', 'pakistan']
print('10.0.0.5'.split('.')) # ['10', '0', '0', '5']
```

The separator itself is removed from the result. Splitting an IP address on `.` is a good example of how this helps with security-related text.

### `join()`

The opposite of `split()`. It **joins** the strings in a collection into **one string**, putting a separator between them. The separator is the string you call `join()` on.

```python
words = ['secure', 'coding', 'rocks']

print(' '.join(words))    # secure coding rocks
print('-'.join(words))    # secure-coding-rocks
```

All items in the collection must be strings.

---

## 7. Checking the start or end

### `startswith(prefix)`

Returns a **boolean** saying whether the string **starts with** the given prefix.

```python
print(s.startswith('good'))     # True
print(s.startswith('bad'))      # False
```

### `endswith(suffix)`

Returns a **boolean** saying whether the string **ends with** the given suffix.

```python
print(s.endswith('pakistan'))   # True
print(s.endswith('lahore'))     # False
```

These are handy for checking things like file extensions (`.txt`, `.py`) or URL prefixes (`https://`).

---

## 8. Searching and counting

### `find(substring)`

Returns the **index of the first occurrence** of the substring, or **`-1`** if it is not found.

```python
print(s.find('morning'))    # 5
print(s.find('xyz'))        # -1
```

`-1` means "not found", so check for it before using the result as an index.

### `count(substring)`

Returns the **number of non-overlapping occurrences** of a substring in the string.

```python
print(s.count('o'))     # 3
print(s.count('an'))    # 1
```

---

## 9. Summary table

| Method | What it does | Example result |
|--------|--------------|----------------|
| `upper()` | All uppercase | `GOOD MORNING PAKISTAN` |
| `lower()` | All lowercase | `good morning pakistan` |
| `capitalize()` | First character capital, the rest lowercase | `Python rocks` |
| `title()` | First letter of each word capital | `Good Morning Pakistan` |
| `isupper()` | Are all letters uppercase? | `True` / `False` |
| `islower()` | Are all letters lowercase? | `True` / `False` |
| `strip()` | Removes leading and trailing characters (whitespace by default) | `admin` |
| `replace(old, new)` | Replaces all occurrences | `good evening pakistan` |
| `split(sep)` | Splits into a list | `['good', 'morning', 'pakistan']` |
| `join()` | Joins a collection into one string | `secure-coding-rocks` |
| `startswith(prefix)` | Does it start with the prefix? | `True` / `False` |
| `endswith(suffix)` | Does it end with the suffix? | `True` / `False` |
| `find(sub)` | Index of first match, or `-1` | `5` |
| `count(sub)` | Number of matches | `3` |

---

## 10. Method chaining

Because each method returns a new string, you can call another method on the result straight away. This is called **chaining**.

```python
messy = '  GOOD Morning  '
print(messy.strip().lower())    # good morning
```

Python runs the methods from left to right: first `strip()`, then `lower()` on its result.

---

## 11. Why this matters in cybersecurity

- **Cleaning input** with `strip()` and `lower()` before comparing it.
- **Splitting log lines** and IP addresses with `split()`.
- **Searching for keywords** in logs or web responses with `find()`, `count()` and the `in` operator.
- **Checking file types and URLs** with `startswith()` and `endswith()`.
- **Rebuilding text** from parts with `join()`.
- **Replacing** unwanted characters in data.

---

## 12. Common mistakes

- Expecting a method to **change the original** string. It returns a new one, so store the result.
- Forgetting the **parentheses**: `s.upper` without `()` does not run the method.
- Forgetting that `strip()` does **not** remove spaces in the middle of a string.
- Using the result of `find()` without checking for `-1`.
- Using `join()` on a list that contains numbers (all items must be strings).
- Forgetting that the separator in `join()` goes **before** the dot: `'-'.join(words)`.
- Forgetting that comparisons are **case-sensitive**.