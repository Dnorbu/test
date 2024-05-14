def main():
    # Ask the user to input their age
    age = int(input("Enter your age: "))
    
    # Ask the user to input whether they are a student or not
    student_input = input("Are you a student? (yes/no): ").lower()
    
    # Check if the user is eligible for a discount based on age and student status
    if age <= 12:
        print("You are eligible for a discount.")
    elif age >= 13 and age <= 18 and student_input == 'yes':
        print("You are eligible for a discount.")
    else:
        print("You are not eligible for a discount.")

if __name__ == "__main__":
    main()
