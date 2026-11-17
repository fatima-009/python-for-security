# String Concatenation

## 1. What is string concatenation?

Joining pieces of text together is one of the most common things you do with strings: building a message, a file path, a URL or a log line.

Joining strings end to end is called **string concatenation**. In Python you do it with the plus (`+`) operator.

```python
first = 'Good'
second = "Morning"

print(first + ' ' + second)   # Good Morning
print(first + second)         # GoodMorning
```

Important points:

- Python joins the strings **exactly as they are**. It does not add spaces for you. If you want a space, add it yourself as a separate string (`' '`), as in the first example.
- The result is a **new string**. The original strings are not changed (strings are immutable).
- You can chain as many strings as you like in one expression.

---

## 2. Repeating strings with `*`

Multiplying a string by an **integer** repeats it that many times.

```python
word = 'ho'
print(word * 3)    # hohoho

print('-' * 20)    # --------------------
```

The second example is a handy way to print a line or divider in a program's output. The number must be an integer, and the result is again a new string.

---

## 3. Concatenating strings with numbers

Concatenation works **only between strings**. If you try to join a string and a number, Python raises a `TypeError`.

```python
user = 'Sara Khan'
level = 4

user + level
```

Error:

```
TypeError: can only concatenate str (not "int") to str
```

### Why does this happen?

Python does **not automatically convert** other types into strings when concatenating. `+` between two numbers adds them, and `+` between two strings joins them, so Python refuses to guess what you mean when you mix the two.

### The fix: `str()`

Convert the number into a string first with the built-in `str()` function. It returns the **string version** of a value and does **not change the original** value.

```python
print(user + str(level))     # Sara Khan4
```

The original `level` is still an integer:

```python
print(level, type(level))    # 4 <class 'int'>
print(type(str(level)))      # <class 'str'>
```

Notice the result `Sara Khan4`: there is no space, because none was added. You would write `user + ' ' + str(level)` to get a space.

---

## 4. Shorthand operators: `+=` and `*=`

### `+=` (concatenate and assign)

`+=` performs concatenation and assignment in **one step**.

```python
label = user
label += str(level)
print(label)    # Sara Khan4
```

`label += str(level)` means exactly the same as `label = label + str(level)`.

### `*=` (repeat and assign)

`*=` repeats a string and stores the result back in the same variable.

```python
beep = 'ab'
beep *= 4
print(beep)     # abababab
```

`beep *= 4` is the same as `beep = beep * 4`.

### An important detail

Both `+=` and `*=` **create a new string** and assign it to the variable. They do **not** modify the original string, because strings are immutable. The variable simply points to the new result.

---

## 5. Why this matters in cybersecurity

- Building **URLs** and **file paths** from parts (for example, a host name and a path).
- Creating **log messages** and reports from several pieces of text.
- Repeating characters to format **banners and separators** in tool output.

---

## 6. Common mistakes

- Trying to join a string and a number with `+` (`TypeError`). Use `str()` or an f-string (see the interpolation notes).
- Forgetting to add spaces between joined strings.
- Multiplying a string by a decimal number such as `'ha' * 2.5` (the multiplier must be an integer).
- Assuming `+=` edits the old string. It builds a new one.

---

## 7. Key takeaways

- **Concatenation** joins strings with `+`. **Repetition** repeats a string with `*` and an integer.
- Python never adds spaces for you, and the originals are never modified.
- A string and a number cannot be joined with `+` without converting the number with `str()`.
- `+=` and `*=` combine the operation and assignment, and they create new strings.

---

## Practice ideas

1. Join your first name and last name with a space between them using `+`.
2. Print a line of 30 equal signs using `*`.
3. Try joining a string and a number with `+`, read the error, then fix it with `str()`.
4. Build a sentence with `+=`, adding a new word each time.