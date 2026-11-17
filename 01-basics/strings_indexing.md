# Strings length and String Immutability

## 1. Length of a string with `len()`

`len()` is a built-in function that returns the **number of characters** in a string.

```python
text = 'Python is fun'
print(len(text))   # 13
```

All characters count, including **spaces** and punctuation. That is why `Python is fun` has 13 characters (12 letters and spaces plus the two spaces between words: 6 + 1 + 2 + 1 + 3 = 13).

---

## 2. Indexing

Each character in a string has a position called an **index**. Indexing lets you access one character at a time.

### Zero-based indexing

Counting starts at **0**, not 1. So the first character has index `0`, the second has index `1`, and so on.

| Character | S | e | c | u | r | i | t | y |
|-----------|---|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Negative index | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

To get a character, write the string (or its variable) followed by the index in **square brackets**.

```python
word = 'Security'

print(word[0])   # S
print(word[4])   # r
```

### Negative indexing

Negative numbers count **from the end**. `-1` is the last character, `-2` is the second-to-last, and so on. This is very useful when you want the end of a string and do not know its length.

```python
print(word[-1])   # y
print(word[-2])   # t
```

### Index errors

If you ask for an index that does not exist, for example `word[20]`, Python raises an `IndexError`. The valid positions run from `0` to `len(word) - 1`, or from `-1` down to `-len(word)`.

---

## 3. Mutable and immutable values

A value in Python is either:

- **Mutable**: it can be **changed after it is created**.
- **Immutable**: it **cannot be changed** once it is created.

**Strings are immutable.** So are integers, floats and booleans. (Other immutable types come in later lessons.)

---

## 4. Reassignment is not the same as modification

This is the part that confuses many beginners.

You **can** point a variable at a brand-new value. This is called **reassignment**. The old string is not changed. The variable just stops pointing to it and points to a new string instead.

```python
status = 'open'
status = 'closed'
print(status)   # closed
```

What you **cannot** do is change the string **itself**, by replacing, adding or removing individual characters inside it.

```python
status = 'closed'
status[0] = 'C'
```

This raises:

```
TypeError: 'str' object does not support item assignment
```

### How to "change" a string then?

Because the original cannot be edited, you create a **new** string based on it and (if you like) assign that new string back to the variable. String methods and concatenation, covered in the next lessons, are the tools for this.

### Why immutability?

- Strings stay **safe and predictable**: no other part of the program can secretly change them.
- Python can **reuse** identical strings efficiently in memory.
- Immutable values can be used safely in places that need stable data, such as dictionary keys (covered later).

---

## 5. Common mistakes

- Forgetting that indexing starts at **0**.
- Trying to change a character with `word[0] = 'X'`.
- Writing a single backslash in a Windows path (`'D:\Projects'`), which can be read as an escape sequence.
- Forgetting that `in` is case-sensitive.
- Expecting `len()` to ignore spaces. It counts them.