<div align="center">

# 🐍 Python Programming Mastery

### A structured, hands-on journey from Python fundamentals to real-world application development

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![OOP](https://img.shields.io/badge/Paradigm-OOP-brightgreen?style=for-the-badge)](https://docs.python.org/3/tutorial/classes.html)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Chapters](https://img.shields.io/badge/Chapters-11-orange?style=for-the-badge)](.)
[![Projects](https://img.shields.io/badge/Projects-1-red?style=for-the-badge)](./PROJECT%201)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](.)

</div>

---

## 🚀 Elevator Pitch

This repository is a **comprehensive, chapter-by-chapter Python curriculum** that goes far beyond passive reading. Every concept is reinforced immediately with dedicated practice problem sets, and the learning arc culminates in a fully functional **Snake-Water-Gun game** shipped with both a polished CLI interface and a desktop GUI built with Tkinter.

> Whether you're a recruiter evaluating Python depth, a developer looking for clean reference implementations, or a learner following the same path — this repo demonstrates **disciplined progression**, **clean code habits**, and the ability to translate algorithmic thinking into shipped software.

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

## 📚 Curriculum Overview

The repository is structured as an 11-chapter course, each containing **concept files** and a companion **Practice Set**:

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

## ✨ Key Features

- **📖 Structured Learning Path** — 11 logically ordered chapters ensure progressive complexity and zero knowledge gaps.
- **🏋️ Practice-First Philosophy** — Every chapter has its own `Practice Set` folder with solved problems, reinforcing theory with real code execution.
- **🎮 Capstone Project: Snake Water Gun Game** — A complete mini-project delivered in *three iterations*:
  - `main.py` — Full CLI version with input validation and descriptive win/loss logic.
  - `main_shorted.py` — Algorithmically refactored version using arithmetic difference to eliminate redundant conditionals.
  - `project2.py` — Feature-complete **Tkinter GUI** with labeled buttons, live result display, and colour-coded win/draw/lose feedback.
- **📂 File I/O Deep Dive** — Chapter 9 goes beyond basics: includes real-world tasks like log file mining (`mineLogFile.py`), poem writer, multiplication table generator, and in-place file replacement.
- **🔁 OOP Progression** — Chapters 10–11 build from first-principles class creation all the way to multi-level inheritance, `super()` chaining, and Python's dunder-method operator overloading.
- **🔬 Algorithm Insight** — `main_shorted.py` includes inline comments explaining the arithmetic trick (`computer - you`) used to collapse 6 conditionals into 1, demonstrating analytical refactoring skill.

---

## 🏗️ Architecture Deep Dive

### PROJECT 1 — Snake Water Gun (Three Implementations)

```
┌─────────────────────────────────────────────────────────────┐
│                    SNAKE WATER GUN GAME                      │
│                                                             │
│  v1: main.py           v2: main_shorted.py                  │
│  ─────────────         ───────────────────                  │
│  • dict lookup         • Same dict lookup                   │
│  • Explicit 6-branch   • Single arithmetic check:           │
│    if/elif chain         (computer - you) == -1 or 2        │
│  • Input validation                                         │
│                                                             │
│  v3: project2.py  ── Tkinter GUI ──                         │
│  ┌────────────────────────────┐                             │
│  │   [Snake] [Water] [Gun]    │  ← Button Frame             │
│  │   You chose: Snake         │  ← Dynamic Labels           │
│  │   Computer chose: Water    │                             │
│  │   You Win! 🎉              │  ← Colour-coded result      │
│  └────────────────────────────┘                             │
└─────────────────────────────────────────────────────────────┘
```

**Game Logic (all versions):**  
`snake (1) > water (-1)` · `water (-1) > gun (0)` · `gun (0) > snake (1)`

The elegant refactor in `main_shorted.py` maps these rules to arithmetic:  
```python
# You Lose when: (computer - you) ∈ {-1, 2}
if (computer - you) == -1 or (computer - you) == 2:
    print("You Lose")
else:
    print("You Win")
```

> 💡 **[Visual Suggestion]** Insert a GIF of the Tkinter GUI in action here — demonstrating the button click, real-time label update, and green/blue/red result colours.

---

## 📁 Repository Structure

```
Python-Programming/
│
├── Chapter 1/                        # Hello World & Syntax Basics
│   ├── first.py
│   └── Practice_Set/                 # Problems 1–4
│
├── Chapter 2 - Variable_Datatype/    # Variables, Operators, Input
│   ├── 01_variable.py
│   ├── 02_dataTypes.py
│   ├── 03_rules_variable.py
│   ├── 04_operators.py
│   ├── 05_type.py
│   ├── 06_input.py
│   └── Practice Set/                 # Problems 1–6
│
├── Chapter 3 - String/               # String Slicing & Methods
│   ├── 01_introToString.py
│   ├── 02_negative_slicing.py
│   ├── 03_slicingWithSkipValue.py
│   ├── 04_str_functions.py
│   ├── 05_escape_seq.py
│   └── Practice Set/                 # Problems 1–3
│
├── Chapter 4 - Lists & Tuples/       # Mutable vs Immutable Sequences
│   ├── 01_list.py  02_list_methods.py
│   ├── 03_tuple.py  04_tuple_methods.py
│   └── Practice Set/                 # Problems 1–3
│
├── Chapter 5 - Dictionary&Sets/      # Key-Value Stores & Set Algebra
│   ├── 01_dict.py  ...  07_setoperations.py
│   └── Practice_Set/                 # Q1–Q6
│
├── Chapter 6 - Conditional Expression/  # if/elif/else Logic
│   ├── 01_conditionals.py
│   └── Practice_Set/                 # Q1–Q5
│
├── Chapter 7 - Loops/                # while, for, break/continue
│   ├── 01_loops.py  ...  06_break_continue.py
│   └── Practice Set/                 # Q1–Q9
│
├── Chapter 8 - Functions_Recursions/ # Functions, Defaults, Recursion
│   ├── 01_function.py  ...  04_recursion.py
│   └── Practice Set/                 # Q1–Q5
│
├── Chapter 9 File/                   # File I/O & Context Managers
│   ├── 01_file.py  ...  05_withStmt.py
│   └── Practice Set/                 # mineLogFile, poem, tableOfThree, replaceFile …
│
├── Chapter 10 - OOPs/                # Classes, self, __init__
│   ├── 01_class.py  02_selfPara.py  03_constructor.py
│   └── Practice Set/                 # Q1
│
├── Chapter 11 - inheritance/         # Inheritance, super(), Overloading
│   ├── inheritance.py
│   ├── multiLevelInheritance.py
│   ├── superMethod.py
│   ├── class_method.py
│   └── operator_overloading.py
│
├── PROJECT 1/                        # 🎮 Snake Water Gun Game
│   ├── main.py                       # CLI — full logic with validation
│   ├── main_shorted.py               # CLI — arithmetic refactor
│   └── project2.py                   # GUI  — Tkinter desktop app
│
├── demo.ipynb                        # Jupyter Notebook demo
├── log.txt / poem.txt / tables/      # Sample data files for Ch9 exercises
└── README.md
```

---

## ⚙️ Installation & Usage

### Prerequisites

- Python **3.8+** installed ([download](https://www.python.org/downloads/))
- `tkinter` is bundled with standard Python installations on Windows/macOS. On Linux, install with:
  ```bash
  sudo apt-get install python3-tk
  ```

### Clone the Repository

```bash
git clone https://github.com/nadim-altaf/Python-Programming.git
cd Python-Programming
```

### Set Up a Virtual Environment *(recommended)*

```bash
# Create
python -m venv .venv

# Activate (macOS / Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### Run Any Chapter Script

```bash
# Example — run the string functions demo
python "Chapter 3 - String/04_str_functions.py"

# Example — run the recursion examples
python "Chapter 8 - Functions_Recursions/04_recursion.py"
```

### Run the Project

```bash
# CLI version (with input validation)
python "PROJECT 1/main.py"
# > Enter your choice: snake

# CLI refactored version
python "PROJECT 1/main_shorted.py"

# GUI version (Tkinter desktop app)
python "PROJECT 1/project2.py"
```

> 💡 **[Visual Suggestion]** Insert a terminal GIF of the CLI game here — showing a user typing `snake`, the computer's random choice printing, and "You Win!" output.

---

## 🔭 Future Scope

The following enhancements would elevate this from a learning repository to a production-grade portfolio piece:

1. **Score Tracker & Session History** — Persist win/loss/draw counts across game rounds to a JSON or SQLite database using the File I/O skills from Chapter 9.
2. **Unit Tests with `pytest`** — Add a `tests/` directory with parameterised test cases for the game logic, demonstrating TDD practices valued in engineering roles.
3. **Packaging with `pyproject.toml`** — Convert PROJECT 1 into an installable CLI tool (`pip install snake-water-gun`) to showcase understanding of modern Python packaging.
4. **Data Analysis Chapter** — Add a Chapter 12 introducing `pandas` and `numpy`, bridging pure Python knowledge to the Data Science / ML stack.
5. **CI/CD Pipeline** — Add a GitHub Actions workflow (`.github/workflows/ci.yml`) to auto-lint with `flake8` and run tests on every push, demonstrating DevOps awareness.
6. **Enhanced GUI** — Extend `project2.py` with animated icons, a round counter, and a high-score display to showcase more advanced Tkinter layout management.
7. **Jupyter Notebook Walkthroughs** — Expand `demo.ipynb` with inline explanations, visualisations, and markdown cells to act as an interactive textbook counterpart to the chapter scripts.

---

## 👤 Author

**Nadim Altaf**  
*Aspiring Machine Learning Engineer & Data Scientist*

[![GitHub](https://img.shields.io/badge/GitHub-nadim--altaf-181717?style=flat-square&logo=github)](https://github.com/nadim-altaf)

---

<div align="center">

*If you found this repository helpful, please consider giving it a ⭐ — it helps others discover it!*

</div>
