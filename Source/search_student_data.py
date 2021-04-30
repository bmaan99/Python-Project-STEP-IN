"""This is a file which contains the search function for the database
This function is used to search for a student using the roll number from user input"""


def search_student(roll_number):
    """This function is used to search for a student using the roll number from user input"""
    with open("data.txt", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.strip().split(",")
            if roll_number == line[0]:
                print("\nDetails Of the student")
                print("Roll Number of Student :", roll_number)
                print("Name of Student:", line[1])
                print("Phone Number of Student:", line[2])
                return True
        print("No Such Student in the data")
        file.close()
        return False
