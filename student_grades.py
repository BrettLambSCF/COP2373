import csv

def student_grades():
    student_amt = int(input("Please type the amount of students you want to enter: "))

    #Opens a file called grades.csv in write mode and with closes it automatically when the program finishes
    with open("grades.csv", "w", newline="") as file:

        #Create the CSV writer object, use writer to add rows to file
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        #Loop repeats for every student the teacher says they want to enter
        for student in range(student_amt):

            #To show which student is now being asked about
            print("\nPlease enter the information for student", student + 1)

            #Asks for all the student's info
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            exam_one = int(input("Exam 1 Grade: "))
            exam_two = int(input("Exam 2 Grade: "))
            exam_three = int(input("Exam 3 Grade: "))

            #Writes that info into a row on the CSV file
            writer.writerow([first_name, last_name, exam_one, exam_two, exam_three])

student_grades()