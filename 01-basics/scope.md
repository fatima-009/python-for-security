# Scope in Python


## 1. What is scope?

**Scope determines where you can use a variable in your code.**

A variable does not exist everywhere in a program. Where it is created decides where it can be used. Python has several scope rules, but for now the lecture focuses on the two most important ones: **local scope** and **global scope**.

---

## 2. Global scope

A variable created **outside a function** has **global scope**. You can use it **both inside and outside functions**.

```python
discount_rate = 0.2
```

`discount_rate` is global because it is created outside any function.

---

## 3. Local scope

A variable created **inside a function** has **local scope**. You can use it **only inside that function**. It is created when the function runs and is not available once the function is finished.

**Function parameters are local variables too.**

---

## 4. Local and global scope together

```python
discount_rate = 0.2

def calculate_discount(price):
    discount = price * discount_rate
    return discount

print(calculate_discount(80))    # 16.0
print(discount_rate)             # 0.2
print(discount)                  # NameError: name 'discount' is not defined
```

Let us look at each variable:

| Variable | Created | Scope | Where it can be used |
|----------|---------|-------|----------------------|
| `discount_rate` | Outside the function | **Global** | Inside and outside `calculate_discount` |
| `price` | As a parameter | **Local** | Only inside `calculate_discount` |
| `discount` | Inside the function | **Local** | Only inside `calculate_discount` |

- The function **can read** the global `discount_rate`, and so can the second `print()` call.
- `price` and `discount` are available **while the function runs**, but **not outside it**.
- The last `print()` raises a **`NameError`** because `discount` is not defined in the global scope. The same happens for `price`:

```python
print(price)    # NameError: name 'price' is not defined
```

A `NameError` is the usual sign that you are trying to use a variable **outside its scope** (or that you misspelled its name).

---

## 5. How arguments are passed

Python passes arguments **by assignment**.

When you call a function, **each parameter becomes a local name** that initially **refers to the object supplied as its argument**. Python does **not automatically copy** that object.

In other words, the parameter and the variable you passed in start out as **two names for the same object**.

---

## 6. Reassigning a parameter

**Reassigning a parameter makes that local name refer to a different object.** It does **not** change the variable you passed to the function.

```python
def triple_number(number):
    number = number * 3
    print(number)    # 45

original = 15
triple_number(original)
print(original)      # 15
```

Step by step:

1. When `triple_number(original)` is called, both `number` and `original` initially refer to the integer `15`.
2. The assignment `number = number * 3` makes the **local** parameter `number` refer to a **new** object, `45`.
3. The variable `original` still refers to `15`. Printing it after the call shows that its value did **not** change.

Think of names as **labels**. The function moved its own label (`number`) to a new object. The other label (`original`) stayed where it was.

---

## 7. Extras: more things to know about scope

The lecture notes that Python has additional scope rules. These short examples are an extra, so you recognize them when you see them.

### A local variable can have the same name as a global one

A variable created inside a function is a **new local variable**, even if a global variable has the same name. The global one is not touched.

```python
level = 'global'

def show_level():
    level = 'local'
    print(level)

show_level()       # local
print(level)       # global
```

Using the same name for both can be confusing, so it is better to choose different names.

### Changing a global variable inside a function

Assigning to a name inside a function creates a **local** variable. If you try to **change** a global number that way, Python raises an error:

```python
total = 0

def add_five_bad():
    total += 5

add_five_bad()
# UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
```

Because the function assigns to `total`, Python treats `total` as local for the **whole function**. Reading it before giving it a value fails.

To change the global variable, declare it with the **`global`** keyword:

```python
total = 0

def add_five():
    global total
    total += 5

add_five()
add_five()
print(total)       # 10
```

The `global` keyword should be used **sparingly**. Passing values in as arguments and sending results back with `return` is usually clearer and safer.

### Reading before assigning

The same error appears when a function reads a name and later assigns to it:

```python
def broken():
    print(counter)
    counter = 1

broken()
# UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
```

### Passing a list: same object, no copy

Since Python does not copy the object, **changing the object itself** inside a function affects the original. This is visible with a list (lists are covered in a later lesson):

```python
def add_item(items):
    items.append('scan')

tasks = ['recon']
add_item(tasks)
print(tasks)       # ['recon', 'scan']
```

But **reassigning** the parameter does not change the original, just like with the number earlier:

```python
def reassign_list(items):
    items = ['other']

tasks2 = ['recon']
reassign_list(tasks2)
print(tasks2)      # ['recon']
```

The difference: `items.append(...)` **changes the shared object**, while `items = [...]` only **moves the local label** to a new object.

### Names inside functions do not clash

Two different functions, or a function and the global code, can use the same local names without affecting each other:

```python
def area(width, height):
    result = width * height
    return result

result = 'outside'
print(area(2, 3), result)    # 6 outside
```

---

## 8. Summary table

| | Global scope | Local scope |
|---|--------------|-------------|
| Created | Outside any function | Inside a function (including its parameters) |
| Can be used | Inside and outside functions | Only inside that function |
| Lifetime | While the program runs | Only while the function runs |
| Example | `discount_rate = 0.2` | `price`, `discount` |
| Using it outside | Works | `NameError` |

| Situation | Result |
|-----------|--------|
| Function **reads** a global variable | Works |
| Function **assigns** to a name | Creates a new **local** variable |
| Function **reassigns** a parameter | Original variable is unchanged |
| Function **changes a shared object** (like a list) | Original object changes |

---

## 9. Why this matters in cybersecurity

- **Predictable code**: local variables stop a function from accidentally changing values elsewhere in your script.
- **Avoiding bugs**: knowing that parameters are local helps you understand why a function's changes do not leak out.
- **Safe configuration**: global values, such as a timeout or a target list, can be read by functions without being passed every time.
- **Debugging**: a `NameError` or `UnboundLocalError` often points to a scope problem.
- **Reusable tools**: functions with their own local variables can be reused without side effects.

---

## 10. Common mistakes

- Trying to use a **local variable outside its function** (`NameError`).
- Expecting a function to **change the original variable** when it reassigns a parameter.
- **Forgetting `return`** and expecting a local result to be available outside.
- Assigning to a global name inside a function and getting an **`UnboundLocalError`**.
- Using the **same name** for a local and a global variable without noticing.
- Overusing the `global` keyword instead of arguments and `return`.
- Forgetting that changing a shared **object** (like a list) inside a function **does** affect the original.