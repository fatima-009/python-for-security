# String Slicing

"What Is String Slicing and How Does It Work?".

---

## 1. Quick recap: indexing

Each character in a string has a position called an **index**, starting from **0**. A single character is accessed with square brackets. Negative indexes count from the end.

The string used in all the examples below is `'Cyber Security'` (14 characters, including the space):

| Character | C | y | b | e | r | (space) | S | e | c | u | r | i | t | y |
|-----------|---|---|---|---|---|---------|---|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| Negative | -14 | -13 | -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

```python
text = 'Cyber Security'

print(text[0])    # C
print(text[6])    # S
print(text[-1])   # y
```

Indexing gives **one** character. Slicing gives a **portion** of the string.

---

## 2. What is string slicing?

**String slicing** lets you extract a part of a string, or work with only a specific section of it. The basic syntax is:

```python
string[start:stop]
```

The `start` and `stop` indexes are separated by a **colon** (`:`).

```python
text = 'Cyber Security'
print(text[1:4])    # ybe
```

### The stop index is not included

This is the most important rule of slicing. `[1:4]` starts at index `1` and goes **up to, but not including, index `4`**. So it takes indexes 1, 2 and 3, which are `y`, `b` and `e`.

A useful way to remember it: the number of characters you get is `stop - start`. Here that is `4 - 1 = 3`.

---

## 3. Leaving out start or stop

You can leave out either index and Python fills in a default:

- No `start`: Python starts from the **beginning** (index `0`).
- No `stop`: Python goes to the **end** of the string.

### Omitting start

```python
print(text[:7])     # Cyber S
```

This takes everything from index `0` up to, but not including, index `7`.

### Omitting stop

```python
print(text[8:])     # curity
```

This takes everything from index `8` to the end of the string.

### Omitting both

```python
print(text[:])      # Cyber Security
```

With both left out, you get the **whole string** (a copy of it).

---

## 4. Slicing does not change the original

Slicing creates a **new string**. The original is untouched, because strings are immutable.

```python
print(text[8:])     # curity
print(text)         # Cyber Security
```

Even after slicing, `text` still holds the full original string. You also cannot use a slice to modify a string:

```python
text[0:3] = 'XYZ'
```

```
TypeError: 'str' object does not support item assignment
```

---

## 5. The step parameter

Slicing has a third, optional part called **step**. It sets the **increment between each index** in the slice. The full syntax is:

```python
string[start:stop:step]
```

With a step of `2`, Python takes every second character.

```python
print(text[0:14:2])   # CbrScrt
```

This starts at index `0`, stops before `14`, and moves two positions at a time. The characters picked are at indexes 0, 2, 4, 6, 8, 10 and 12: `C`, `b`, `r`, `S`, `c`, `r`, `t`.

Another example, taking every third character of the whole string:

```python
print(text[::3])      # CeSut
```

If `step` is not given, it defaults to `1` (every character).

---

## 6. Reversing a string with step `-1`

A negative step makes Python move **backwards**. If you set the step to `-1` and leave `start` and `stop` empty, you get the whole string in **reverse order**.

```python
print(text[::-1])     # ytiruceS rebyC
```

This is a very common Python trick. For example, you can use it to check whether a word reads the same backwards (a palindrome):

```python
word = 'level'
print(word == word[::-1])   # True
```

---

## 7. Negative indexes inside slices

Negative indexes work inside slices too, which makes it easy to cut from the end of a string.

```python
print(text[-8:])      # Security
print(text[:-9])      # Cyber
```

- `text[-8:]` means "from the 8th character from the end, to the end".
- `text[:-9]` means "from the start, up to (but not including) the 9th character from the end".

---

## 8. Slicing is forgiving

Unlike indexing, slicing does **not** raise an error when you go past the end of the string. Python simply stops at the end.

```python
print(text[2:100])    # ber Security
```

An empty slice, where start and stop are the same, gives an **empty string**:

```python
print(text[5:5] == '')   # True
```

Compare this with indexing: `text[100]` would raise an `IndexError`, but `text[2:100]` works fine.

---

## 9. Summary of the syntax

| Syntax | Meaning | Example result |
|--------|---------|----------------|
| `s[start:stop]` | From `start` up to, not including, `stop` | `text[1:4]` gives `ybe` |
| `s[:stop]` | From the beginning up to `stop` | `text[:7]` gives `Cyber S` |
| `s[start:]` | From `start` to the end | `text[8:]` gives `curity` |
| `s[:]` | The whole string | `Cyber Security` |
| `s[start:stop:step]` | Take every `step`-th character | `text[0:14:2]` gives `CbrScrt` |
| `s[::-1]` | Reverse the string | `ytiruceS rebyC` |

---

## 10. Why this matters in cybersecurity

- Extracting a **part of a log line**, such as a date, an IP address or a status code.
- Cutting a **file extension** or a **domain** from a longer string.
- Looking at the **first few characters** of a hash or a token.
- Checking **prefixes and suffixes** of strings.
- Reversing text, which appears in simple CTF puzzles.