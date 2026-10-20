# Data Types, type() and isinstance()

This file focuses on understanding the ideas, with only short examples.


## 1. What is a data type?

A data type describes **what kind of value** a piece of data is, and therefore **what you can do with it**. You can add two numbers, but adding a number to a piece of text makes no sense. You can split text into words, but you cannot split the number 5.

Every value in Python has a type. Python decides the type automatically from the value you assign (this is called dynamic typing), so you never have to declare it yourself. Even so, you must know the types, because many bugs come from using the wrong one.

> In Python, a variable does not have a type. The **value** has a type. The variable is just a name pointing to it, which is why one name can later point to a value of a different type.


## 2. Common data types

### Basic (single-value) types

   Type      |                         Meaning                               | Example              |

- `int`      | Whole numbers, positive or negative, no decimal point         | `22`, `-7`, `443`    | 

- `float`    | Numbers with a decimal point                                  | `3.14`, `-0.5`       |

- `str`      | Text, written inside quotes                                   | `"hello"`, `'admin'` |

- `bool`     | Only two possible values: `True` or `False`                   | `True`               |

- `NoneType` | The special value `None`, meaning "nothing" or "no value yet" | `None`               |

### Collection types (hold many values)

These are covered in detail later in the course. For now, just recognize them.

   Type   |                  Meaning                  |      Example                    |

- `list`  | Ordered collection that can be changed    | `[80, 443, 22]`                 |

- `tuple` | Ordered collection that cannot be changed | `(80, 443)`                     |

- `dict`  | Key-value pairs                           | `{"user": "admin", "port": 22}` |

- `set`   | Unordered collection of unique items      | `{1, 2, 3}`                     |

### Notes on each basic type

**int**: Python integers can be as large as your memory allows, so there is no overflow problem. In security work, ints are used for port numbers, counts and sizes.

**float**: Floats are approximations. Some decimal numbers cannot be stored exactly, which is why `0.1 + 0.2` gives `0.30000000000000004` and not exactly `0.3`. This is normal behaviour in almost every programming language, not a Python bug.

**str**: Text can use single or double quotes. Both work the same. Anything inside quotes is text, even if it looks like a number, so `"443"` is a string and `443` is an integer. This difference matters a lot (see section 5).

**bool**: Used for yes/no decisions, such as "is the port open?" or "is the password correct?". The words `True` and `False` must start with a capital letter.

**None**: Represents the absence of a value. A function that does not return anything gives back `None`.

### Mutable and immutable

Types are either **mutable** (can be changed after creation) or **immutable** (cannot). `int`, `float`, `str`, `bool` and `tuple` are immutable, while `list`, `dict` and `set` are mutable. This explains why strings behave differently from lists later on.


## 3. The type() function

`type()` is a built-in function that **tells you the type of a value or variable**. It is one of the most useful debugging tools for a beginner: when code behaves strangely, check the type first.

```python
port = 443
print(type(port))     # <class 'int'>
```

The output shows `class` because in Python every type is a class. You do not need to understand classes yet. Just read `<class 'int'>` as "this is an int".

What it is good for:

- Checking what kind of data you are actually dealing with.
- Discovering why an operation fails (for example, text where a number was expected).
- Seeing that data from outside the program (like user input) is a string by default.

Also remember that `type()` shows the type of the **value at that moment**. If the variable is reassigned to something else, the type changes too.


## 4. The isinstance() function

`isinstance()` **checks whether a value is of a particular type and answers True or False**. It takes two arguments: the value, then the type to check against.

```python
port = 443
print(isinstance(port, int))     # True
print(isinstance(port, str))     # False
```

### Checking against several types

You can give a tuple of types. The result is `True` if the value matches any one of them.

```python
print(isinstance(3.5, (int, float)))   # True
```

`isinstance()` is generally the recommended way to check types inside programs.

### A surprising detail: bool is a kind of int

In Python, `bool` is built on top of `int`, with `True` behaving like `1` and `False` like `0`. So:

```python
print(isinstance(True, int))    # True
print(type(True) == int)        # False
```

This is a good example of why the two functions can give different answers.


## 5. Why types matter

The same operator behaves differently depending on the types involved.

```python
print(5 + 5)         # 10  (numbers are added)
print("5" + "5")     # 55  (text is joined together)
print("5" + 5)       # TypeError (cannot mix text and number)
```

A very common situation: data typed by a user or read from a file arrives as **text**, even if it looks like a number. It must be converted before doing maths.

### Type conversion (casting)

Python has functions to convert between types, named after the types themselves: `int()`, `float()`, `str()` and `bool()`.

```python
port_text = "443"
port_number = int(port_text)
print(type(port_number))    # <class 'int'>
```

Notes on conversion:

- Converting text that is not a valid number, such as `int("hello")`, causes a `ValueError`.
- `int(3.9)` gives `3`: the decimal part is cut off, not rounded.
- Converting to `bool`: empty things (`0`, `""`, `None`, empty collections) become `False`, almost everything else becomes `True`.


## 6. Relevance to cybersecurity

| Data | Typical type |

| Port number | `int` |
| IP address | `str` |
| Is the port open? | `bool` |
| List of usernames to test | `list` of `str` |
| Result of a scan, with fields | `dict` |
| Response time in seconds | `float` |

Network and web tools constantly convert between text and numbers, so checking types with `type()` and `isinstance()` saves a lot of debugging time.


## 7. Common mistakes

- Treating a numeric string as a number, for example `"10" * 2` gives `"1010"`, not `20`.
- Writing `true` or `false` in lowercase instead of `True` and `False`.
- Forgetting that `input()` always returns a string.
- Assuming `type()` can be used to quickly check against subtypes. Use `isinstance()` for that.
- Expecting float results to be exact.


## 8. Key takeaways

- A data type defines what a value is and what operations are allowed on it.
- The common types are `int`, `float`, `str`, `bool` and `None`, plus collections like `list`, `tuple`, `dict` and `set`.
- `type()` tells you the type of a value. `isinstance()` checks whether a value matches a type and returns `True` or `False`.
- Values often need converting with `int()`, `float()`, `str()` or `bool()`.
- Checking types early is one of the easiest ways to find bugs.
