def classify_age():
    age = int(input("Enter your age (pls don't lie): ")) 

    if age < 0:
        print("Invalid age. Please enter a non-negative number, you filthy animal.")
    elif age <= 12:
        print("You're a Child.")
    elif age <= 19:
        print("You're a Teen.")
    elif age <= 64:
        print("You're an Adult.")
    else:
        print("You're are a Senior.")


classify_age()
