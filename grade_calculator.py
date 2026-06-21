"""
Student Grade Calculator
-------------------------
A simple Python program that takes a student's name and marks,
validates the input, calculates the grade using if-elif-else logic,
and displays an encouraging message based on the grade.
Grading Logic:
    A : 90 - 100
    B : 80 - 89
    C : 70 - 79
    D : 60 - 69
    F : 0  - 59
"""
def calculate_grade(marks):
    """
    Takes marks (0-100) and returns a tuple: (grade, message)
    Uses if-elif-else statements to decide the grade.
    """
    if marks >= 90:
        grade = "A"
        message = "Excellent! Outstanding performance!"
    elif marks >= 80:
        grade = "B"
        message = "Very Good! Keep it up!"
    elif marks >= 70:
        grade = "C"
        message = "Good job! You can do even better!"
    elif marks >= 60:
        grade = "D"
        message = "You passed! Work a bit harder next time."
    else:
        grade = "F"
        message = "Don't give up! Practice more and you'll improve."
    return grade, message

def get_valid_marks():
    """
    Repeatedly asks the user for marks until a valid number
    between 0 and 100 is entered. Uses a while loop + try/except
    for basic error handling.
    """
    while True:
        user_input = input("Enter marks (0-100): ")
        try:
            marks = float(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100. Try again.\n")
            continue
        return marks

def get_valid_name():
    """
    Keeps asking for the student's name until a non-empty value
    is provided.
    """
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            print("Name cannot be empty. Please try again.\n")
            continue
        return name

def display_result(name, marks, grade, message):
    """
    Prints the final formatted result for the student.
    """
    print("\n RESULT FOR {}:".format(name.upper()))
    print("Marks: {:.0f}/100".format(marks))
    print("Grade: {}".format(grade))
    print("Message: {}\n".format(message))

def main():
    """
    Main program loop. Allows checking multiple students until
    the user chooses to stop.
    """
    print("=" * 40)
    print("   STUDENT GRADE CALCULATOR")
    print("=" * 40)
    while True:
        name = get_valid_name()
        marks = get_valid_marks()
        grade, message = calculate_grade(marks)
        display_result(name, marks, grade, message)
        again = input("Do you want to check another student? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the Grade Calculator! Goodbye 👋")
            break
        print()

if __name__ == "__main__":
    main()
