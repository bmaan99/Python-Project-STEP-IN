"""This is a file which contains the remove function for the database
This function is used to remove for a student using the roll number from user input"""


def remove_student():
    """This function is used to remove for a student using the roll number from user input"""
    roll_number = input("Enter the roll number of student to Remove: ")
    with open("data.txt", "r") as file:
        data = file.readlines()
        for line in data:
            org_line = line
            line = line.strip().split(",")
            if roll_number == line[0]:
                data.remove(org_line)
                print("Student '"+line[1]+"' Removed from the Data")
        file.close()

        with open("data.txt", "w") as file:
            file.writelines(data)
            file.close()
