# Create an empty dictionary for student data
D1 = {}

# Get number of students
n = int(input('Enter number of Students: '))

# Input data for each student
for _ in range(n):
    key = input('Enter Student Name: ')
    print('Enter student id and their Marks in Physics, Chemistry and Math respectively: ')
    
    # Create a dictionary to store student data (ID, marks)
    student_data = {}
    student_data['Student_ID'] = (input('Enter Student ID: '))
    student_data['P_Marks'] = int(input('Enter Physics marks: '))
    student_data['C_Marks'] = int(input('Enter Chemistry marks: '))
    student_data['M_Marks'] = int(input('Enter Math marks: '))
    
    # Store student data in the main dictionary D1
    D1[key] = student_data

# Display the dictionary D1
print("\nStudent Data Dictionary (D1):")
print(D1)

flag=True
while flag:
    # Menu for user options
    print("\nEnter 1, 2, 3, 4 to print the following:")
    print('1. Student with highest Marks in Physics')
    print('2. Student with lowest marks in Chemistry')
    print('3. Given a student name, print his/her percentage and determine if he/she has failed or passed')
    print('4. Given a Student_ID find the corresponding name.')

    # Take user choice
    ch = int(input())

    # Option 1: Student with highest Marks in Physics
    if ch == 1:
        highest_physics_marks = -1  # Set to a low number initially
        top_student = ''
        for name, data in D1.items():
            if data['P_Marks'] > highest_physics_marks:
                highest_physics_marks = data['P_Marks']
                top_student = name
        print(f"Student with highest marks in Physics: {top_student} with {highest_physics_marks} marks.")

    # Option 2: Student with lowest Marks in Chemistry
    elif ch == 2:
        lowest_chemistry_marks = 101  # Set to a high number initially
        bottom_student = ''
        for name, data in D1.items():
            if data['C_Marks'] < lowest_chemistry_marks:
                lowest_chemistry_marks = data['C_Marks']
                bottom_student = name
        print(f"Student with lowest marks in Chemistry: {bottom_student} with {lowest_chemistry_marks} marks.")

    # Option 3: Given a student name, print his/her percentage and pass/fail status
    elif ch == 3:
        student_name = input("Enter student name: ")
        if student_name in D1:
            student = D1[student_name]
            total_marks = student['P_Marks'] + student['C_Marks'] + student['M_Marks']
            percentage = (total_marks / 300) * 100  # Calculate percentage out of 300
            status = "Pass" if percentage >= 40 else "Fail"  # Assuming 40% is passing
            print(f"{student_name}'s Percentage: {percentage:.2f}% - Status: {status}")
        else:
            print("Student not found.")

    # Option 4: Given a Student_ID, find the corresponding name
    elif ch == 4:
        student_id = (input("Enter Student ID: "))
        found = False
        for name, data in D1.items():
            if data['Student_ID'] == student_id:
                print(f"Student with ID {student_id} is {name}.")
                found = True
                break
        if not found:
            print("Student ID not found.")

    # Invalid option
    else:
        print('Wrong input!')
    print('Do you want to try again? If no, press 0')
    ch=(input())
    if ch==0: 
        flag=False
