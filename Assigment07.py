# ------------------------------------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Structured Error Handling Example
# ChangeLog (Who,When,What):
# SSimpers,5.30.2023,Created script
# ------------------------------------------------------------------------------------------------------- #

import pickle  # imports code from Pickle module

# Data  ------------------------------------------------------------------------------------------------- #
strFileName = 'FileData.dat'  # A string corresponding to the file name
lstEntry = []  # A list that will store a row of user entered data


# Processing  ------------------------------------------------------------------------------------------- #
def write_data_to_file(file_name, list_of_data):
    """ Writes data from a list to a binary file

    :param file_name: (string) with name of file:
    :param list_of_data: (list) of data:
    :return: nothing
    """
    file = open(file_name, "wb")  # opens file in "write binary" mode, creates file if non-existent
    pickle.dump(list_of_data, file)  # saves list to binary file
    file.close()


def read_data_from_file(file_name):
    """ Reads data from a binary file into a list

    :param file_name: (string) with name of file:
    :return: list_of_data: (list) of data
    """
    file = open(file_name, "rb")  # opens file in "read binary" mode
    list_of_data = pickle.load(file)  # reads list from binary file and assigns to list variable
    return list_of_data


# Presentation (Input/Output)  -------------------------------------------------------------------------- #
def get_user_input():
    """  Gets name and grade to be stored in a list

    :return: (string, float) with name and grade data
    """
    name = str(input(" Enter student name: "))  # capture user input for student name
    while True:
        try:
            grade = float(input(" Enter grade (0 - 100): "))  # capture user input for grade
        except ValueError:  # error from converting letters to float
            print(" Please only enter numbers!")
            continue
        else:
            if grade < 0 or grade > 100:  # only accept numbers from 0 to 100
                print(" Please enter a number from 0 to 100!")
            else:
                break
    entry = [name, grade]  # assigns user input name and grade to list
    return entry


# Presentation (Main Body of Script) -------------------------------------------------------------------- #
lstEntry = get_user_input()  # get user input and assign to list
print("\n List prior to pickling: ", lstEntry)  # print the list prior to pickling
write_data_to_file(strFileName, lstEntry)  # pickle the list into binary file
print(" List after pickling and unpickling: ", read_data_from_file(strFileName))  # print the unpickled list
input("\n Press 'Enter' to exit")
