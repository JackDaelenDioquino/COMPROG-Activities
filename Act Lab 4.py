def assign_grade():
    score = int(input("Enter the student's score (0-100): "))

    if score < 0 or score > 100:
        print("Enter a value between 0 and 100, quit wasting my time!")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")


assign_grade()
