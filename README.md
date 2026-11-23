# Python for Security

This repo contains my study notes, workshop solutions and (later) mini projects.

I write the notes in my own words, with my own examples, and I run the code to check the outputs.

## Repository structure

```
python-for-security/
├── README.md
├── 01-basics/            # study notes (Markdown)
│   ├── intro.md
│   ├── variables.md
│   ├── data_types.md
│   ├── declaring_variables.md
│   ├── comments.md
│   ├── strings.md
│   ├── string_concatenation.md
│   ├── string_interpolation.md
│   ├── string_slicing.md
│   ├── string_methods.md
│   ├── integers_and_floats.md
│   ├── augmented_assignments.md
│   ├── fstring_number_formatting.md
│   ├── conditional_statements.md
│   └── truthy_falsy_and_boolean_operators.md
└── workshops/            # hands-on workshops (code + write-up)
    ├── report-card/
    ├── employee-card/
    ├── employee-profile-validator/
    └── bill-splitter/
```

## Study notes

All notes are in [`01-basics`](01-basics/).

### Getting started

| Notes | What it covers |
|-------|----------------|
| [Introduction to Python](01-basics/intro.md) | What Python is, what it is used for, tools to set up, and related skills |
| [Variables](01-basics/variables.md) | Variables, naming conventions and `print()` |
| [Declaring variables](01-basics/declaring_variables.md) | Assignment, dynamic typing, multiple assignment, constants and type hints |
| [Data types](01-basics/data_types.md) | Common data types, `type()` and `isinstance()` |
| [Comments](01-basics/comments.md) | `#` comments, docstrings and good commenting habits |

### Strings

| Notes | What it covers |
|-------|----------------|
| [Strings and immutability](01-basics/strings.md) | Quotes, multiline strings, escape sequences, `in`, `len()`, indexing and immutability |
| [String concatenation](01-basics/string_concatenation.md) | `+`, `*`, `str()`, `+=` and `*=` |
| [String interpolation](01-basics/string_interpolation.md) | f-strings and expressions inside `{}` |
| [String slicing](01-basics/string_slicing.md) | `[start:stop:step]`, negative indexes and reversing |
| [String methods](01-basics/string_methods.md) | `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `join()`, `find()` and more |

### Numbers and math

| Notes | What it covers |
|-------|----------------|
| [Integers and floats](01-basics/integers_and_floats.md) | Arithmetic operators, rounding errors, `int()`, `float()`, `round()`, `abs()` and `pow()` |
| [Augmented assignments](01-basics/augmented_assignments.md) | `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` and bitwise forms |
| [Formatting numbers in f-strings](01-basics/fstring_number_formatting.md) | `.2f`, rounding for display and `round()` vs formatting |

### Booleans and conditionals

| Notes | What it covers |
|-------|----------------|
| [Conditional statements](01-basics/conditional_statements.md) | Comparison operators, `if`, `else`, `elif` and indentation |
| [Truthy/falsy values and boolean operators](01-basics/truthy_falsy_and_boolean_operators.md) | `bool()`, `and`, `or`, `not` and short-circuiting |

## Workshops

Each workshop has its own folder with the final code and a README that explains every step.

| Workshop | Topics practiced |
|----------|------------------|
| [Report Card](workshops/report-card/) | Data types (`str`, `bool`, `int`, `float`), `type()`, `isinstance()` |
| [Employee Card](workshops/employee-card/) | String concatenation, `+=`, `str()`, f-strings and slicing |
| [Employee Profile Validator](workshops/employee-profile-validator/) | String methods, method chaining, `.find()`, `.split()`, `.join()` and `.count()` |
| [Bill Splitter](workshops/bill-splitter/) | Numbers, `+=`, percentages, division and `round()` |

## Progress

- [x] Introduction to Python
- [x] Variables and data types
- [x] Strings
- [x] Numbers and mathematical operations
- [ ] Booleans and conditionals
  - [x] Comparison operators and `if` / `else` / `elif`
  - [x] Truthy and falsy values, `and`, `or`, `not`
  - [ ] Identity operators
- [ ] Loops
- [ ] Functions
- [ ] File handling

## Tools

- Python 3
- VS Code
- Git and GitHub

## Related repositories

- `overthewire-writeups`: my OverTheWire (Bandit and Natas) write-ups. ( repo: `https://github.com/fatima-009/overthewire-writeups`.)

## Disclaimer

All security-related code here is for educational purposes
and tested only on systems I own or in authorized labs.
