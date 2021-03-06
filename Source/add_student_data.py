"""This is a file which has the add function for database and function to get roll number list
The add function adds a student using the roll number, name and phone number from user input
The get roll list function returns the list of roll number
"""


def get_roll_list():
    """This function returns the list of roll number check students that are already added"""
    roll_list = []
    with open("data.txt", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.strip().split(",")
            roll_list.append(line[0])
    return roll_list


def add_student(roll_number, name, phone_number):
    """This function student using the roll number, name and phone number from user input
    It validates the inputs from user and adds it to the database"""
    roll_list = get_roll_list()
    while True:
        if roll_number in roll_list:
            print("\nThis student already exists!!\n")
            return False

        elif not phone_number.isnumeric() or len(phone_number) != 10:
            print("\nPhone number is not Valid\nMust be a number and 10 characters long\n")
            return False

        else:
            with open("data.txt", "a") as file:
                file.write("\n" + roll_number + "," + name + "," + phone_number)
                print("Student '"+name+"' added to the file")
                file.close()
                return True
