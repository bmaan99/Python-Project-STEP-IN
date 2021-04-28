"""This is the file with print function to call other functions of the module
This function prints details of all students in a tabular format
"""


def print_students():
    """This function prints details of all students in a tabular format"""
    # Opening file by using the with
    with open("data.txt", "r") as file:
        data = file.readlines()
        print("-" * 74)
        print("|{:^20}|{:^30}|{:^20s}|".format("Roll Number", "Name of Student", "Phone Number"))
        for line in data:
            line = line.strip().split(",")
            roll_number = line[0]
            name = line[1]
            phone = line[2]
            print("|{:^20}|{:^30}|{:^20s}|".format(roll_number, name, phone))
        print("-" * 74)
        file.close()
