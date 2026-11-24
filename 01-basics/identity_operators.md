# Identity Operators


## 1. Variables and objects

In Python, a **variable is a name that refers to an object**. The object itself lives in memory, and the variable is just a label pointing to it.

**Identity operators** check whether **two operands refer to the same object**.

| Operator | Meaning |
|----------|---------|
| `is` | Returns `True` if both operands refer to the **same object**, otherwise `False` |
| `is not` | Returns the **opposite** result of `is` |

---

## 2. Identity vs equality

These two ideas are easy to mix up:

| Operators | What they compare |
|-----------|-------------------|
| `==` and `!=` | **Values** (do they look the same?) |
| `is` and `is not` | **Object identity** (are they literally the same object?) |

A simple comparison: two printed copies of the same book are **equal** (same content), but they are not the **same object**. Only one physical copy is identical to itself.

**Rule of thumb:** use `==` and `!=` when comparing **number or string values**. Use `is` and `is not` mainly for `None`, `True` and `False`.

---

## 3. `None`

`None` represents the **absence of a value**. It is the only value of the `NoneType` data type.

```python
print(type(None))    # <class 'NoneType'>
```

It is commonly used to mean "no value yet", "nothing found" or "no answer given".

### Singletons

Three objects you can safely check with identity operators are **`None`**, **`True`** and **`False`**. Each one is a **singleton**, meaning there is **exactly one object** of each in the whole program. So checking `is None` always works reliably.

---

## 4. Checking for `None`

Use **`is None`** to check whether a value is **missing**, and **`is not None`** to check whether a value is **present**.

```python
token = None

print(token is None)        # True
print(token is not None)    # False
```

After giving the variable a value, the results flip:

```python
token = 'abc123'

print(token is None)        # False
print(token is not None)    # True
```

### A realistic example

Functions often return `None` when they find nothing. Identity operators are the correct way to test for this:

```python
def find_user(name):
    users = {'sara': 'admin'}
    return users.get(name)

result = find_user('omar')
print(result, result is None)          # None True

result = find_user('sara')
print(result, result is not None)      # admin True
```

(The function and dictionary are shown only for the idea. You will learn functions and dictionaries later.)

---

## 5. `None` is falsy, but it is not `False`

`None` is **falsy**, but it is **not the same object** as `False`. This matters when a value can have three states. For example, an answer can be:

- `True` for yes
- `False` for no
- `None` if no answer has been given yet

```python
answer = False

if answer is None:
    print('No answer yet')
else:
    print('An answer was given')    # An answer was given
```

`False` is a real answer (the answer is "no"), so the code reports that an answer was given. With `None`:

```python
answer = None

if answer is None:
    print('No answer yet')          # No answer yet
else:
    print('An answer was given')
```

### Why not just use `if not answer`?

`if not answer` treats **both** `False` and `None` the same way, because both are falsy. The identity check can **tell the difference** between a negative answer and a missing answer.

```python
for answer in (True, False, None):
    print(answer, '| not answer:', not answer, '| is None:', answer is None)
```

```
True  | not answer: False | is None: False
False | not answer: True  | is None: False
None  | not answer: True  | is None: True
```

Notice that `False` and `None` give the same result for `not answer`, but different results for `is None`.

---

## 6. Checking for `True` and `False`

Identity can also check for the boolean objects specifically:

```python
answer = True

print(answer is True)        # True
print(answer is False)       # False
print(answer is not None)    # True
```

And with `False`:

```python
answer = False

print(answer is True)        # False
print(answer is False)       # True
print(answer is not None)    # True
```

These checks ask whether the value is **exactly** `True`, exactly `False`, or **any object other than `None`**. They do **not** simply test truthiness.

### When to use `is True` / `is False`

For ordinary boolean flags, use **direct truth tests**:

```python
is_ready = True

if is_ready:
    print('ready')          # ready

if not is_ready:
    print('not ready')
```

Use `is True` or `is False` only when you must **distinguish a real boolean object from other possible values**, such as an answer that might also be `None`.

---

## 7. `is` is not `==`: a closer look

Because `is` compares objects and `==` compares values, they can give different results.

### Equal values that are different objects

Two lists with the same content are **equal**, but they are **separate objects**:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True   (same values)
print(a is b)    # False  (different objects)
print(a is c)    # True   (c points to the very same object as a)
print(a is not b)    # True
```

The `id()` function shows an object's identity number. Two names that refer to the same object have the same id:

```python
print(id(a) == id(c))    # True
print(id(a) == id(b))    # False
```

(Lists are covered in a later lesson. They are used here only to show the difference between equal and identical.)

### `True` and `False` are not the same as `1` and `0`

Values can be **equal** without being the **same object**:

```python
print(None == False, None is False)    # False False
print(0 == False, 0 is False)          # True False
print(1 == True, 1 is True)            # True False
```

`0 == False` is `True` because Python treats `False` as equal to `0`. But `0 is False` is `False`, because they are different objects.

### Do not use `is` with numbers and strings

Python warns you when you compare with a literal number or string using `is`:

```python
x = 5
print(x is 5)
```

```
SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
```

Whether two equal numbers or strings happen to be the same object depends on how Python manages memory internally, so you cannot rely on it. To compare number or string values, always use `==` and `!=`:

```python
text = 'python'
print(text == 'python')    # True
```

---

## 8. Summary table

| Task | Correct way |
|------|-------------|
| Is a value missing? | `value is None` |
| Is a value present? | `value is not None` |
| Is it exactly `True`? | `value is True` |
| Is it exactly `False`? | `value is False` |
| Does a boolean flag hold a true value? | `if flag:` |
| Are two numbers or strings equal? | `a == b` |
| Are two names the same object? | `a is b` |

---

## 9. Why this matters in cybersecurity

- Checking whether a function **found something** or returned `None` (for example, no matching user or record).
- Telling apart **"no answer yet"** from a **negative result**, such as a scan that has not run versus a scan that found nothing.
- Validating that an **optional setting** was actually provided before using it.
- Avoiding bugs where a falsy value like `0` or `''` is wrongly treated as "missing".

---

## 10. Common mistakes

- Using `==` to check for `None`. Use `is None`.
- Using `is` to compare numbers or strings. Use `==`.
- Confusing `is` with `==` and expecting equal lists to be the same object.
- Using `if not value` when a value of `0`, `''` or `False` is a valid value. Use `is None` instead.
- Writing `is True` for ordinary flags where `if flag:` is cleaner.
- Forgetting that `None` is not the same as `False`, `0` or an empty string.