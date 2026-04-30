<div align="center">

# 🐍 Python Programming

### Learning Python — from the basics to a working project

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![OOP](https://img.shields.io/badge/Paradigm-OOP-brightgreen?style=for-the-badge)](https://docs.python.org/3/tutorial/classes.html)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Chapters](https://img.shields.io/badge/Chapters-11-orange?style=for-the-badge)](.)
[![Projects](https://img.shields.io/badge/Projects-1-red?style=for-the-badge)](./PROJECT%201)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](.)

</div>

---

## About

This is my personal Python learning repository. I worked through 11 topics in order — from `print("Hello World")` to OOP with inheritance — and wrote practice problems after each one to make sure things actually stuck. The whole thing wraps up with a Snake-Water-Gun game that I built three ways: a basic CLI, a refactored CLI, and a Tkinter desktop GUI.

If you're learning Python too, feel free to look around. The chapter scripts and practice sets are all here.

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.x |
| **GUI Framework** | Tkinter (stdlib) |
| **Paradigms** | OOP · Procedural · Functional |
| **Core Concepts** | Data Structures · File I/O · Recursion · Inheritance · Operator Overloading |
| **Dev Tools** | Git · VS Code / any Python IDE |

---

## 📚 Chapters

11 chapters, each with concept scripts and a practice set:

| Chapter | Topic | Key Concepts |
|---------|-------|-------------|
| 1 | **Introduction** | First Python script, `print()`, basic syntax |
| 2 | **Variables & Data Types** | `int`, `float`, `str`, `bool`, operators, `input()`, type casting |
| 3 | **Strings** | Slicing, negative indexing, skip-value slicing, built-in string methods, escape sequences |
| 4 | **Lists & Tuples** | List methods, mutability vs immutability, tuple methods |
| 5 | **Dictionaries & Sets** | CRUD operations, set operations (union, intersection, difference), `len()` |
| 6 | **Conditional Expressions** | `if / elif / else`, nested conditions, ternary expressions |
| 7 | **Loops** | `while`, `for`, `for…else`, `break`, `continue`, list construction via loops |
| 8 | **Functions & Recursion** | Defining functions, parameters vs arguments, default arguments, recursive algorithms |
| 9 | **File I/O** | Reading/writing files, `append` mode, `with` statement, log file mining, file manipulation |
| 10 | **OOP** | Classes, `self` parameter, constructors (`__init__`) |
| 11 | **Inheritance & Advanced OOP** | Single & multi-level inheritance, `super()`, class methods, operator overloading |

---

## ✨ What's in Here

- **📖 Chapters in order** — 11 topics, each building on the last. No jumps, no gaps.
- **🏋️ Practice sets** — Every chapter has a `Practice Set` folder with solved problems. Writing code > just reading it.
- **🎮 Capstone project: Snake Water Gun** — built three times:
  - `main.py` — CLI with input validation and basic win/loss logic.
  - `main_shorted.py` — Same game, but refactored to replace six if/elif branches with a single arithmetic check.
  - `project2.py` — Tkinter GUI with buttons, live result labels, and colour-coded feedback.
- **📂 Chapter 9 File I/O** — Goes past the basics. Includes log file mining (`mineLogFile.py`), a poem writer, a multiplication table generator, and in-place file replacement.
- **🔁 OOP across two chapters** — Chapter 10 covers classes and constructors from scratch. Chapter 11 adds multi-level inheritance, `super()`, class methods, and operator overloading.

---

## 🎮 PROJECT 1 — Snake Water Gun

Three versions of the same game, each with a different approach.

- **`main.py`** — Standard CLI. Takes user input, picks a random computer choice, and prints the result with clear win/loss messages.
- **`main_shorted.py`** — Same logic, fewer lines. The choices are mapped to integers (`snake = 1`, `water = -1`, `gun = 0`), and the winner is determined with one arithmetic check instead of six branches.
- **`project2.py`** — Tkinter GUI. Three buttons, two label updates per click, and colour-coded result text.

**The arithmetic trick in `main_shorted.py`:**

`snake (1) > water (-1)` · `water (-1) > gun (0)` · `gun (0) > snake (1)`

Those win/loss relationships produce a consistent pattern when you subtract:

```python
# You Lose when: (computer - you) ∈ {-1, 2}
if (computer - you) == -1 or (computer - you) == 2:
    print("You Lose")
else:
    print("You Win")
```

Six conditionals collapsed into one. It's a clean observation worth keeping around.

---

## 📁 Repository Structure

```
Python-Programming/
│
├── Chapter 1/                            # Hello World & Syntax Basics
│   └── first.py
├── Chapter 1 Practice_Set/               # Problems 1–4
│
├── Chapter 2 - Variable_Datatype/        # Variables, Operators, Input
│   ├── 01_variable.py
│   ├── 02_dataTypes.py
│   ├── 03_rules_variable.py
│   ├── 04_operators.py
│   ├── 05_type.py
│   └── 06_input.py
├── Chapter 2 Practice Set/               # Problems 1–6
│
├── Chapter 3 - String/                   # String Slicing & Methods
│   ├── 01_introToString.py
│   ├── 02_negative_slicing.py
│   ├── 03_slicingWithSkipValue.py
│   ├── 04_str_functions.py
│   └── 05_escape_seq.py
├── Chapter 3 Practice Set/               # Problems 1–3
│
├── Chapter 4 - Lists & Tuples/           # Mutable vs Immutable Sequences
│   ├── 01_list.py  02_list_methods.py
│   └── 03_tuple.py  04_tuple_methods.py
├── Chapter 4 Practice Set/               # Problems 1–3
│
├── Chapter 5 - Dictionary&Sets/          # Key-Value Stores & Set Algebra
│   └── 01_dict.py  ...  07_setoperations.py
├── Chapter 5 Practice_Set/               # Q1–Q6
│
├── Chapter 6 - Conditional Expression/   # if/elif/else Logic
│   └── 01_conditionals.py
├── Chapter 6 Practice_Set/               # Q1–Q5
│
├── Chapter 7 - Loops/                    # while, for, break/continue
│   └── 01_loops.py  ...  06_break_continue.py
├── Chapter 7 Practice Set/               # Q1–Q9
│
├── Chapter 8 - Functions_Recursions/     # Functions, Defaults, Recursion
│   └── 01_function.py  ...  04_recursion.py
├── Chapter 8 Practice Set/               # Q1–Q5
│
├── Chapter 9 File/                       # File I/O & Context Managers
│   └── 01_file.py  ...  05_withStmt.py
├── Chapter 9 Practice Set/               # mineLogFile, poem, tableOfThree, replaceFile …
│
├── Chapter 10 - OOPs/                    # Classes, self, __init__
│   └── 01_class.py  02_selfPara.py  03_constructor.py
├── Chapter 10 Practice Set/              # Q1
│
├── Chapter 11 - inheritance/             # Inheritance, super(), Overloading
│   ├── inheritance.py
│   ├── multiLevelInheritance.py
│   ├── superMethod.py
│   ├── class_method.py
│   └── operator_overloading.py
│
├── PROJECT 1/                            # 🎮 Snake Water Gun Game
│   ├── main.py                           # CLI — full logic with validation
│   ├── main_shorted.py                   # CLI — arithmetic refactor
│   └── project2.py                       # GUI  — Tkinter desktop app
│
├── demo.ipynb                            # Jupyter Notebook demo
├── log.txt / poem.txt / tables/          # Sample data files for Ch9 exercises
└── README.md
```

---

## ⚙️ Installation & Usage

### Prerequisites

- Python **3.8+** ([download](https://www.python.org/downloads/))
- `tkinter` is bundled on Windows/macOS. On Linux:
  ```bash
  sudo apt-get install python3-tk
  ```

### Clone

```bash
git clone https://github.com/nadim-altaf/Python-Programming.git
cd Python-Programming
```

### Virtual Environment *(optional but recommended)*

```bash
# Create
python -m venv .venv

# Activate (macOS / Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### Run a chapter script

```bash
python "Chapter 3 - String/04_str_functions.py"
python "Chapter 8 - Functions_Recursions/04_recursion.py"
```

### Run the project

```bash
# Full CLI
python "PROJECT 1/main.py"

# Refactored CLI
python "PROJECT 1/main_shorted.py"

# Tkinter GUI
python "PROJECT 1/project2.py"
```

---

## 🔭 What's Next

A few things I'd like to add when I get the time:

1. **Score tracking** — save win/loss/draw counts to a JSON file between rounds.
2. **Tests** — a `tests/` folder with `pytest` cases for the game logic.
3. **Packaging** — turn PROJECT 1 into an installable CLI with `pyproject.toml`.
4. **Chapter 12: Data Analysis** — an intro to `pandas` and `numpy` as a natural next step.
5. **CI** — a simple GitHub Actions workflow to lint and run tests on push.
6. **Better GUI** — round counter, high-score display, maybe some icons.
7. **Notebook walkthroughs** — flesh out `demo.ipynb` with proper explanations per chapter.

---

## 👤 Author

**Nadim Altaf**  
*Aspiring Machine Learning Engineer & Data Scientist*

[![GitHub](https://img.shields.io/badge/GitHub-nadim--altaf-181717?style=flat-square&logo=github)](https://github.com/nadim-altaf)

---

<div align="center">

*If this was helpful, a ⭐ is always appreciated.*

</div>
