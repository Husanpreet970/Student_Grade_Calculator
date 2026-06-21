# 🎓 Student Grade Calculator

A beginner-friendly Python program built as part of **Week 2: Making Decisions & Repeating Tasks in Python**. It takes a student's name and marks, validates the input, calculates a letter grade (A–F), and displays an encouraging message based on performance.

---

## 📌 Project Overview & Objectives

This project demonstrates core Python fundamentals covered in Week 2:
- **If-elif-else statements** for decision-making (grading logic)
- **Comparison operators** to check mark ranges
- **While loops** for input validation (keeps asking until valid input is given)
- **For/while loop** for repeating the program for multiple students
- **Functions** to organize and reuse code
- **Basic error handling** using `try/except` to catch non-numeric input

**Objective:** Build a working command-line tool that mimics a real-world grading system, while practicing decision-making and loop structures in Python.

---

## ⚙️ Setup & Installation Instructions

### Requirements
- Python 3.6 or higher
- No external libraries needed (uses only Python's built-in features)

### Steps to Run
1. Clone or download this repository:
   ```bash
   git clone <your-repo-url>
   cd grade_calculator
   ```
2. Run the program:
   ```bash
   python3 grade_calculator.py
   ```
   (On Windows, you may use `python grade_calculator.py`)
3. Follow the on-screen prompts to enter a student's name and marks.

---

## 🧩 Code Structure Explanation

The program is organized into clear, reusable **functions**, each with a single responsibility:

| Function | Purpose |
|---|---|
| `calculate_grade(marks)` | Core grading logic. Uses **if-elif-else** to map marks to a grade (A–F) and returns a matching encouraging message. |
| `get_valid_marks()` | Uses a **while loop** combined with **try/except** to repeatedly prompt the user until they enter a valid number between 0 and 100. |
| `get_valid_name()` | Uses a **while loop** to ensure the student's name is not left empty. |
| `display_result(name, marks, grade, message)` | Formats and prints the final result block shown to the user. |
| `main()` | The entry point. Ties everything together and uses a **while loop** to allow checking multiple students in a single run. |

### Grading Logic
```
A : 90 - 100  → "Excellent! Outstanding performance! 🌟"
B : 80 - 89   → "Very Good! Keep it up! 👍"
C : 70 - 79   → "Good job! You can do even better! 😊"
D : 60 - 69   → "You passed! Work a bit harder next time. 💪"
F : 0  - 59   → "Don't give up! Practice more and you'll improve. 🙌"
```
The `calculate_grade()` function checks the marks from highest to lowest using `if marks >= 90`, `elif marks >= 80`, and so on, falling through to `else` for an F grade. This ensures every mark between 0–100 maps to exactly one grade.

---

## ✅ How Technical Requirements Were Met

| Requirement | Where it's implemented |
|---|---|
| Use if-elif-else for grading logic | `calculate_grade()` function |
| Input validation (marks 0-100 only) | `get_valid_marks()` checks `marks < 0 or marks > 100` and re-prompts |
| At least one function | Four functions used: `calculate_grade`, `get_valid_marks`, `get_valid_name`, `display_result`, plus `main()` |
| Encouraging message for each grade | Each branch in `calculate_grade()` returns a unique motivational message |
| While loop for invalid inputs | `get_valid_marks()` and `get_valid_name()` both use `while True:` loops that only `return`/`break` once valid input is received |
| Basic error handling | `try/except ValueError` in `get_valid_marks()` catches non-numeric input (e.g., typing "abc") without crashing the program |

**Bonus feature:** The program loops in `main()` so multiple students can be graded in a single run without restarting the script.

---

## 🖥️ Sample Run

```
========================================
   STUDENT GRADE CALCULATOR
========================================
Enter student name: Priya
Enter marks (0-100): 85

📊 RESULT FOR PRIYA:
Marks: 85/100
Grade: B
Message: Very Good! Keep it up! 👍

Do you want to check another student? (y/n): n

Thank you for using the Grade Calculator! Goodbye 👋
```

### Handling Invalid Input
```
Enter marks (0-100): 150
⚠️  Marks must be between 0 and 100. Try again.

Enter marks (0-100): abc
⚠️  Invalid input! Please enter a number.

Enter marks (0-100): 45
```

---

## 📸 Screenshots

> Screenshots of the working application should be placed in the `screenshots/` folder and referenced here, e.g.:
>
> ![Sample Run](screenshots/sample_run.png)
> ![Invalid Input Handling](screenshots/invalid_input.png)

---

## 📁 Repository Structure

```
grade_calculator/
├── README.md          # This documentation file
├── grade_calculator.py # Main program
├── test_cases.txt      # Manual test cases and results
└── screenshots/        # Screenshots of the working app
```

---

## 🧪 Testing

See [`test_cases.txt`](./test_cases.txt) for 12 manually run test cases covering:
- All five grade boundaries (A, B, C, D, F)
- Invalid marks (negative, over 100, non-numeric)
- Empty name handling
- Multi-student loop continuation
- Decimal mark input

All 12 test cases passed. ✅

---

## 🚧 Challenges Faced / Notes

- Decided to accept **decimal marks** (e.g., 88.5) using `float()` instead of `int()`, since real-world marks are sometimes given with decimals. The displayed marks are still shown as whole numbers using formatting.
- Used a **separate function for name validation** (`get_valid_name`) in addition to marks validation, to make the program more robust even though it wasn't explicitly required.
- Added a loop in `main()` so the program can be used for multiple students without restarting — useful for a teacher grading an entire class.
