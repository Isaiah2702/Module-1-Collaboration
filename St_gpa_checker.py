#Author: Isaiah Snelling
#File: St_gpa_checker.py
#Description: This program accepts student names and GPAs, then determines if the student qualifies for either the Dean's List (GPA >= 3.5) or the Honor Roll (GPA >= 3.25). The program continues accepting records until 'ZZZ' is entered as the last name.

def main():
    while True:
        # Get student last name
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ").strip()
        if last_name.upper() == 'ZZZ':
            break
        
        # Get student first name
        first_name = input("Enter student's first name: ").strip()
        
        # Get and validate GPA input
        try:
            gpa = float(input("Enter student's GPA: "))
        except ValueError:
            print("Invalid input. Please enter a numeric GPA.")
            continue
        
        # Determine and print qualifications
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")
        
        print("-")  # Separator for readability

if __name__ == "__main__":
    main()
