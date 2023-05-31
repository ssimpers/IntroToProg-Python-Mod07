# Pickling and Structured Error Handling
**Dev:** *SSimpers*  
**Date:** *5/30/2023*  
**Class:** *Foundations of Programming: Python*  
**Assignment:** *07*  

## Introduction
Placeholder sentence.

## Pickle Module
Placeholder sentence.

Listing 1: Pickle module
```
import pickle  # imports code from Pickle module
```


## Data
Placeholder sentence.

Listing 2: Data
```
# Data  ------------------------------------------------------------------------------------------------- #
strFileName = 'FileData.dat'  # A string corresponding to the file name
lstEntry = []  # A list that will store a row of user entered data
```

## Processing - Writing Data to a File
Placeholder sentence.

Listing 3: Function to write data to a binary file
```
def write_data_to_file(file_name, list_of_data):
    """ Writes data from a list to a binary file

    :param file_name: (string) with name of file:
    :param list_of_data: (list) of data:
    :return: nothing
    """
    file = open(file_name, "wb")  # opens file in "write binary" mode, creates file if non-existent
    pickle.dump(list_of_data, file)  # saves list to binary file
    file.close()
```

## Processing - Reading Data from a File
Placeholder sentence.

Listing 4: Function to read data from a binary file
```
def read_data_from_file(file_name):
    """ Reads data from a binary file into a list

    :param file_name: (string) with name of file:
    :return: list_of_data: (list) of data
    """
    file = open(file_name, "rb")  # opens file in "read binary" mode
    list_of_data = pickle.load(file)  # reads list from binary file and assigns to list variable
    return list_of_data
```

## Input/Output - Get User Inputs
Placeholder sentence.

Listing 5: Function to get user inputs
```
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
```

## Main Body of the Script
Placeholder sentence.

Listing 6: Main body of the script
```
# Presentation (Main Body of Script) -------------------------------------------------------------------- #
lstEntry = get_user_input()  # get user input and assign to list
print("\n List prior to pickling: ", lstEntry)  # print the list prior to pickling
write_data_to_file(strFileName, lstEntry)  # pickle the list into binary file
print(" List after pickling and unpickling: ", read_data_from_file(strFileName))  # print the unpickled list
input("\n Press 'Enter' to exit")
```

## Results
Placeholder sentence.

![Figure 1](/docs/Figure1.png "Figure 1")  
Figure 1: Python script running in PyCharm

![Figure 2](/docs/Figure2.png "Figure 2")  
Figure 2: Python script running in Command Window

![Figure 3](/docs/Figure3.png "Figure 3")  
Figure 3: Data Saved in “FileData.dat” File

## Summary
Placeholder sentence.
