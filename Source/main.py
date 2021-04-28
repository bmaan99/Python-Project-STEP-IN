"""This is the file with main function to call other functions of the module
"""
from print_student_data import print_students
from search_student_data import search_student
from remove_student_data import remove_student
from add_student_data import add_student


def print_start_message():
    """
    Printing Welcome Message And options For This Program
    """
    print("\n\nStudent Database Management System")
    print("""
    Enter 1 : To View Student's List 
    Enter 2 : To Add New Student 
    Enter 3 : To Search Student 
    Enter 4 : To Remove Student
    Enter 5 : To Quit Program
    """)


def main():
    """
    Main method to call all other functions
    It will accept user choices and call functions accordingly
    """
    while True:
        print_start_message()
        user_input = 0
        try:  # Using Exceptions For Validation
            user_input = int(input("Enter your choice > "))  # Will Take Input From User
        except ValueError:
            print("\nThat's Not A Number")  # Error Message
        else:
            print("\n")  # Print New Line

        # Checking Using Option
        if user_input == 1:  # This Option Will Print List Of Students
            print("Details of all students: ")
            print_students()

        elif user_input == 2:  # This Option Will Add New Student In The Data file
            print("Add Student Menu:")
            add_student()

        elif user_input == 3:  # This Option Will Search Student From The Data file
            print("Search Student Menu")
            search_student()

        elif user_input == 4:  # This Option Will Remove Student From The Data file
            print("Remove Student Menu:")
            remove_student()

        elif user_input == 5:
            print("Thanks for using the Student database\nExiting Program.....")
            return

        else:
            print("Please Enter Valid Option")  # Error Message


if __name__ == '__main__':
    main()
