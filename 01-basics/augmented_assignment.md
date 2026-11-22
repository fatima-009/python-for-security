# Augmented Assignments


## 1. What is an augmented assignment?

You have already seen augmented assignment with strings (`+=`). It works with numbers too.

An **augmented assignment** applies an operation to a variable and **stores the result back in the same variable**, all in one step.

The basic syntax is:

```python
variable <operator>= value
```

For numbers, this is a shorter way of writing:

```python
variable = variable <operator> value
```

### Example with and without augmented assignment

Using the augmented form:

```python
my_var = 20
my_var += 8

print(my_var)    # 28
```

The same thing written the long way:

```python
my_var = 20
my_var = my_var + 8

print(my_var)    # 28
```

Both give the same result. The second version simply repeats the variable name.

### Why use augmented assignment?

- It is **shorter** and **easier to read**.
- It updates a variable's value **without repeating the variable name**.
- That reduces **redundancy** and the chance of **typos**. When you write `my_var = my_var + 8`, you could accidentally mistype one of the two names. With `my_var += 8` the name appears only once.

### How to read it

Read `x += 8` as "add 8 to `x` and keep the result in `x`". The same pattern works for the other operators below.

---

## 2. The arithmetic assignment operators

Arithmetic operators all have an augmented form. We have already looked at `+=`, so here are the others.

### Subtraction assignment `-=`

Subtracts the right value from the variable and stores the **difference** back in the variable.

```python
count = 30
count -= 12

print(count)     # 18
```

### Multiplication assignment `*=`

Multiplies the variable by the right value and stores the **product** back in the variable.

```python
product = 9
product *= 6

print(product)   # 54
```

### Division assignment `/=`

Divides the variable by the right value and stores the **result** back in the variable.

```python
price = 90
price /= 4

print(price)     # 22.5
```

Remember that normal division (`/`) always returns a **float**, so the variable becomes a float even when the answer is a whole number:

```python
q = 90
q /= 3

print(q)         # 30.0
print(type(q))   # <class 'float'>
```

### Floor division assignment `//=`

Floor-divides the variable by the right value and stores the result back in the variable. Floor division rounds **down** to the nearest whole value.

```python
total_pages = 47
total_pages //= 6

print(total_pages)    # 7
```

`47 / 6` is about `7.83`, and rounding down gives `7`.

### Modulo assignment `%=`

Computes the **remainder** of the variable divided by the right value and stores it back in the variable.

```python
bits = 29
bits %= 5

print(bits)      # 4
```

`29` divided by `5` is `5` with a remainder of `4`.

### Exponentiation assignment `**=`

Raises the variable to the **power** of the right value and stores the result back in the variable.

```python
power = 3
power **= 4

print(power)     # 81
```

---

## 3. Summary table

| Operator | Name | Long form | Example | Result |
|----------|------|-----------|---------|--------|
| `+=` | Addition assignment | `x = x + n` | `20`, `+= 8` | `28` |
| `-=` | Subtraction assignment | `x = x - n` | `30`, `-= 12` | `18` |
| `*=` | Multiplication assignment | `x = x * n` | `9`, `*= 6` | `54` |
| `/=` | Division assignment | `x = x / n` | `90`, `/= 4` | `22.5` |
| `//=` | Floor division assignment | `x = x // n` | `47`, `//= 6` | `7` |
| `%=` | Modulo assignment | `x = x % n` | `29`, `%= 5` | `4` |
| `**=` | Exponentiation assignment | `x = x ** n` | `3`, `**= 4` | `81` |

---

## 4. Several updates in a row

Augmented assignments are often used to **update a value step by step**, such as a score or a counter. Each line works on the result of the previous one.

```python
score = 0
score += 10      # 10
score -= 3       # 7
score *= 4       # 28

print(score)     # 28
```

They work with floats too:

```python
balance = 250.5
balance -= 20.25

print(balance)   # 230.25
```

---

## 5. Bitwise operators

The lecture also notes that **bitwise operators** have augmented forms. Bitwise operators work on the individual **bits** (the 0s and 1s) of integers. You will study them in more detail later, but here is the full list so you recognize them:

| Operator | Operation |
|----------|-----------|
| `&=` | Bitwise AND |
| `\|=` | Bitwise OR |
| `^=` | Bitwise XOR |
| `<<=` | Shift bits left |
| `>>=` | Shift bits right |

A quick example of each, so the pattern is clear:

```python
n = 12
n &= 10
print(n)     # 8

n = 12
n |= 3
print(n)     # 15

n = 12
n ^= 5
print(n)     # 9

n = 3
n <<= 2
print(n)     # 12

n = 20
n >>= 2
print(n)     # 5
```

Bitwise operations show up in cybersecurity topics such as **permissions, flags, encryption and network masks**, so it is worth knowing they exist. You do not need to memorize them now.

---

## 6. The variable must already exist

An augmented assignment **reads** the variable's current value first, so the variable must have been created earlier. Otherwise Python raises a `NameError`.

```python
total += 1
```

```
NameError: name 'total' is not defined
```

Fix it by giving the variable a starting value first, for example `total = 0`.

---

## 7. It works with strings too

You have already seen `+=` and `*=` with strings. The idea is the same: a new value is built and stored back in the variable.

```python
text = 'Hi'
text += '!'

print(text)      # Hi!
```

Numbers and strings are both **immutable**, so an augmented assignment does not modify the original value. It creates a **new value** and points the variable to it.

---

## 8. Why this matters in cybersecurity

- **Counting** events, such as failed logins or open ports, with `count += 1`.
- Updating **totals and scores** while looping through data.
- **Reducing** a value step by step, for example remaining attempts with `attempts -= 1`.
- Using `%=` and `//=` in simple **ciphers** and calculations.
- Working with **bits and flags** using the bitwise forms.

---

## 9. Common mistakes

- Using an augmented assignment on a variable that has **not been created** yet (`NameError`).
- Writing the operator in the wrong order. It is `+=`, not `=+`. Writing `x =+ 5` assigns positive 5, which is not what you want.
- Forgetting that `/=` always turns the variable into a **float**.
- Confusing `//=` (floor division) with `/=` (normal division).
- Confusing `**=` (power) with `*=` (multiplication).
- Putting a space inside the operator (`+ =`), which is a `SyntaxError`.