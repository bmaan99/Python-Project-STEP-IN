import os
import platform

global listStd  # Making ListStd As Super Global Variable
listStd = []  # List Of Students


def print_students():
    file = open("data.txt", "r")
    data = file.readlines()
    print("_" * 74)
    print("|{:^20}|{:^30}|{:^20s}|".format("Roll Number", "Name of Student", "Phone Number"))
    for line in data:
        line = line.strip().split(",")
        roll_number = line[0]
        name = line[1]
        phone = line[2]
        print("|{:^20}|{:^30}|{:^20s}|".format(roll_number, name, phone))


def add_student():
    roll_number = input("Enter the roll Number of student: ")
    name = input("Enter name of the student: ")
    phone_number = input("Enter phone number of student: ")
    file = open("data.txt", "a")
    file.write("\n" + roll_number + "," + name + "," + phone_number)
    print("Student", name, "added to the file")


def print_start_message():
    # Printing Welcome Message And options For This Program
    print(""" 

      ------------------------------------------------------
     |======================================================| 
     |======== Welcome To Student Management System	========|
     |======================================================|
      ------------------------------------------------------

    Enter 1 : To View Student's List 
    Enter 2 : To Add New Student 
    Enter 3 : To Search Student 
    Enter 4 : To Remove Student """)


def main():
    print_start_message()
    print("Enter your choice > ")
    try:  # Using Exceptions For Validation
        userInput = int(input("Please Select An Above Option: "))  # Will Take Input From User
    except ValueError:
        exit("\nHy! That's Not A Number")  # Error Message
    else:
        print("\n")  # Print New Line

    # Checking Using Option
    if userInput == 1:  # This Option Will Print List Of Students
        print_students()

    elif userInput == 2:  # This Option Will Add New Student In The List
        add_student()

    elif userInput == 3:  # This Option Will Search Student From The List
        srcStd = input("Enter Student Name To Search: ")
        if srcStd in listStd:  # This Condition Searching The Student
            print("\n=> Record Found Of Student {}".format(srcStd))
        else:
            print("\n=> No Record Found Of Student {}".format(srcStd))  # Error Message

    elif userInput == 4:  # This Option Will Remove Student From The List
        rmStd = input("Enter Student Name To Remove: ")
        if rmStd in listStd:  # This Condition Removing The Student From The List
            listStd.remove(rmStd)
            print("\n=> Student {} Successfully Deleted \n".format(rmStd))
            for students in listStd:
                print("=> {}".format(students))
        else:
            print("\n=> No Record Found of This Student {}".format(rmStd))  # Error Message

    elif userInput < 1 or userInput > 4:  # Validating User Option
        print("Please Enter Valid Option")  # Error Message


# brought to you by code-projects.org
# add_student()
print_students()
