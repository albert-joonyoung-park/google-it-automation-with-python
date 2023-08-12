########################################################################
# Module 02: Using Python to Interact with the Operating System
# Week 02

########################################################################
# Practice quizz 1. Writing CSV to a dictionary
########################################################################

import os
import csv

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnaion,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("pointsetta,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the info. about the each row
def contents_of_file(filename):
    return_string = ""

    # Call he function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as file:
        # Read the rows of the file into a dictionary
        # DictReader treats the first row as header
        reader = csv.DictReader(file)
        
        # Process each item of the dictionary
        for row in reader:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string

# Call the function
print(contents_of_file("flowers.csv"))

########################################################################
# Week2
# Practice quizz 2. Process data in csv WITHOUT turning into a dictionary
# How to skip the first header row for processing?
########################################################################

import os
import csv

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,types\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file content and format the info.
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file created above
    with open(filename, "r") as file:
        # Read the rows of the file
        rows = csv.reader(file) # not using DictReader()
        # Process each row, skipping the first header
        for row in list(rows)[1:]: # iterator rows can be converted to list, and slice the list to skip the first row of header
            name, color, types = row # unpack the items in row
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(color,name,types)
    return return_string

def contents_of_file2(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file created above
    with open(filename, "r") as file:
        # Read the rows of the file
        rows = csv.reader(file) # not using DictReader()
        # Skip the first row using built-in next()
        next(rows)
        print("Skipped the first header row using next()...")
        for row in rows:
            name, color, types = row # unpack the items in row
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(color,name,types)
    return return_string
# Call the function to start
print(contents_of_file("flowers2.csv"))
print(contents_of_file2("flowers_next.csv"))

#######################################################################
# QwikLab - csv files and dictionary
# For this lab, imagine you are an IT Specialist at a medium-sized company. 
# The Human Resources Department at your company wants you to find out 
# how many people are in each department. You need to write a Python script 
# that reads a CSV file containing a list of the employees in the organization, 
# counts how many people are in each department, and then generates a report 
# using this information. The output of this script will be a plain text file.
#######################################################################
#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list

employee_list = read_employees('./employees.csv')
#print(employee_list)

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    
    return department_data


dictionary = process_data(employee_list)
#print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

write_report(dictionary, './test_report.txt')

###################################################
# Regular expressions
###################################################

reserved_common = {
    ".": ["Any character", "grep l.rts /usr/share/dict/words",
    """: ["Starting with - circumflex", "grep ^fruit /usr/share/dict/words"],
    }