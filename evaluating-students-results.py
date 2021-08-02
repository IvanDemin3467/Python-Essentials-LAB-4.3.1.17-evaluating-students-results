# This is the Python Essentials 2 LAB 4.3.1.17 evaluating-students-results
# Prof. Jekyll conducts classes with students and regularly makes notes in a text file.
# Each line of the file contains three elements:
# the student's first name, the student's last name,
# and the number of point the student received during certain classes.

from os import strerror

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # This exception is raised in many cases if file contains bad lines
    def __init__(self, message = ""):
        StudentsDataException.__init__(self)
        print("Bad line in file. ", message)
        #quit() # Uncomment to terminate program in case of error


class FileEmpty(StudentsDataException):
    # This exception is raised in a case of empty file
    def __init__(self):
        StudentsDataException.__init__(self)
        print("File empty")
        #quit() # Uncomment to terminate program in case of error


def user_input():
    # This function prompts user to input the name of the file
    while True:
        try:
            s = open(input("Enter student's data filename: "), "rt")
            return s
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno)) 


def evaluate_file(stream):
    # This function evaluates the data in the file and converts it into list
    try:
        line_count = 0      # Store number of lines
        data_structure = [] # Store valuable data from file
        print("Data from file:")
        for line in stream: # Iterate through lines in file
            line_count += 1 # Do not forget to count lines in a file
            
            # Evaluate lines in a file and print them to cmd
            if len(line) == 1:
                raise BadLine("Line is empty")
            print(line, end = "")

            # Read valuable data from lines and evaluate it
            entries = line.split()         # get data from line
            if len(entries) < 3:           # Check for insufficient data
                BadLine("Not enough data in line " + str(line_count))
            elif len(entries) > 3:         # Check for excessive data
                BadLine("Too much data in line " + str(line_count))
            elif not (entries[0].isalpha()\
                      and entries[1].isalpha()): # Check for incorrect full names
                BadLine("Incorrect full name in line " + str(line_count))
            else:                          # Check for incorrect grades
                try:
                    entries[2] = float(entries[2])
                except:
                    BadLine("Incorrect grade in line " + str(line_count))
                    continue
            data_structure.append(entries) # save data to list

        # Evaluate the length of the file
        if line_count == 0:
            raise FileEmpty()

    # Deal with exceptions
    except BadLine:
        pass
    except FileEmpty:
        pass    

    # Return result
    return data_structure


def students_results():
    # This function processes results stored in a list;
    # perfoms grades summation;
    # converts results into a dict;
    # and prints report to cmd
    
    # Read data from file
    stream = user_input()
    data_structure = evaluate_file(stream)

    # Convert list into dict while summing grades
    dict = {}
    for entry in data_structure:
        key = entry[0] + " " + entry[1]
        if key not in dict:
            dict[key] = entry[2]
        else:
            dict[key] += entry[2]
    
    # Sort that dict by key
    # Sorted() requires list, so convert dict into list using .items()
    # Sorted() returns list, so convert list into dict using comprehension
    dict = {k: v for k, v in sorted(dict.items())}

    # Print report to cmd
    print("\nReport:")
    for item in dict.items():
        print(item[0] + "\t" + str(item[1]))
    
    


if __name__ == "__main__":
    students_results()
