# Pickling and Structured Error Handling
**Dev:** *SSimpers*  
**Date:** *5/28/2023*

## Introduction
Placeholder sentence.

## Topic 1
Placeholder sentence.

Listing 1
```
try:
    new_file_name = input("Enter the name of the file you want to make: ")
    if new_file_name.isnumeric():
        raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```


### Subtopic
Placeholder sentence.

## Results
Placeholder sentence.

![Figure 1](/docs/Figure1.png "Figure 1")  
Figure 1: Python script running in PyCharm

![Figure 2](/docs/Figure2.png "Figure 2")  
Figure 2: Python script running in Command Window

![Figure 3](/docs/Figure3.png "Figure 3")  
Figure 3: Data Saved in “AppData.dat” File

## Summary
Placeholder sentence.

## References
1. [Reference Title](https://www.google.com "Reference Title")  
2. [Reference Title](https://www.google.com "Reference Title")  

## GitHub Page
ADD LINK TO WEBSITE
