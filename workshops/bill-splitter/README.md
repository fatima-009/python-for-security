# Bill Splitter Workshop

A workshop in which I practiced numbers and mathematical operations by building a bill splitter. The program adds up the cost of a group meal, calculates a tip, and works out how much each person owes.

## Topics covered in this workshop

| Topic | Used in steps |
|-------|---------------|
| Storing integers in variables | 1, 2 |
| Storing floats in variables (amounts with cents) | 3 |
| Augmented assignment `+=` with numbers | 4, 6 |
| Adding several values in one expression | 4 |
| Printing text together with a number (`print()` with a comma) | 4, 5, 6, 7, 8 |
| Floating-point rounding errors | 4 |
| Calculating a percentage by multiplying with `*` | 5 |
| Division with `/` | 7 |
| Rounding with `round(number, decimals)` | 8 |

## What I built

A program that keeps a running total of a restaurant bill, adds a tip, and divides the final amount between friends.

| Item | Variable | Value | Type |
|------|----------|-------|------|
| Running total (starts at zero) | `running_total` | `0` | `int` |
| Number of friends | `num_of_friends` | `5` | `int` |
| Appetizers | `appetizers` | `42.15` | `float` |
| Main courses | `main_courses` | `68.72` | `float` |
| Desserts | `desserts` | `29.46` | `float` |
| Drinks | `drinks` | `51.83` | `float` |
| Tip percentage | used in `tip` | `0.20` (20%) | `float` |

## Files

| File | Description |
|------|-------------|
| `bill_splitter.py` | The final program |
| `README.md` | Notes on the 8 steps (this file) |

## How to run

```
python bill_splitter.py
```

## Output

```
Total bill so far: 192.16000000000003
Tip amount: 38.43200000000001
Total with tip: 230.59200000000004
Bill per person: 46.11840000000001
Each person pays: 46.12
```

The long decimals in the first four lines are floating-point rounding errors. Rounding at the end gives a clean money amount.

---

## The 8 steps

**Step 1: Create the running total.**
To keep track of the total as costs are added, created a variable that starts at zero.

```python
running_total = 0
```

**Step 2: Store the number of friends.**
The number of people sharing the bill is stored in a variable, to be used later for the split.

```python
num_of_friends = 5
```

**Step 3: Store the cost of each course.**
Because the amounts include cents, they are stored as floats.

```python
appetizers = 42.15
main_courses = 68.72
desserts = 29.46
drinks = 51.83
```

**Step 4: Calculate the total with `+=`.**
The `+=` operator adds a value to an existing variable and updates it in one step. Used it once to add all four costs to `running_total`, then printed the result.

```python
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)
```

```
Total bill so far: 192.16000000000003
```

The output has more decimal digits than expected. Numbers are stored in binary, and many decimal values cannot be represented exactly, which leads to small rounding errors.

**Step 5: Calculate the tip.**
To find a percentage, multiply the total by its decimal equivalent. For a 20% tip the multiplier is `0.20`.

```python
tip = running_total * 0.20
print('Tip amount:', tip)
```

```
Tip amount: 38.43200000000001
```

**Step 6: Add the tip to the total.**
Used `+=` again to add the tip to `running_total`, giving the final amount for the whole group.

```python
running_total += tip
print('Total with tip:', running_total)
```

```
Total with tip: 230.59200000000004
```

**Step 7: Split the bill.**
Divided the total by the number of friends using the `/` operator. Division always returns a float.

```python
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)
```

```
Bill per person: 46.11840000000001
```

**Step 8: Round to two decimal places.**
Money is shown with two decimal places, so the result is rounded with `round()`, which takes the number and the number of decimal places to keep.

```python
each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)
```

```
Each person pays: 46.12
```

---

## How the calculation flows

```
  192.16   cost of the four courses
+  38.43   20% tip (192.16 x 0.20)
= 230.59   total with tip
/      5   friends
=  46.12   each person pays (after rounding)
```

(The values above are shown rounded to two decimals for readability. The program uses the full unrounded numbers until the last step.)