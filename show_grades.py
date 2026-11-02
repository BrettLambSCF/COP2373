import csv

#This program will read the CSV file and then neatly display all its information

def show_grades():

    #Opens the grades.csv file in read mode and 'with' closes it automatically after
    with open("grades.csv", "r") as file:

        #Creates a CSV reader object
        reader = csv.reader(file)

        #Prints the header of our table, '<' means left align the text and the number is the amount of space
        print(f"{'First Name':<14}{'Last Name':<16}{'Exam 1 | ':<6}{'Exam 2 | ':<6}{'Exam 3 ':<6}")
        print("---------------------------------------------------------")
        #Skips the first row in the file because it doesn't need to show again
        next(reader)
        #The loop goes through each row/student in the file and prints out their info as a table
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

show_grades()