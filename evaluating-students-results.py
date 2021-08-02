# This is the Python Essentials 2 LAB 4.3.1.17 evaluating-students-results
# Prof. Jekyll conducts classes with students and regularly makes notes in a text file.
# Each line of the file contains three elements:
# the student's first name, the student's last name,
# and the number of point the student received during certain classes.

from os import strerror

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Write your code here.
    def __init__(self, message = ""):
        StudentsDataException.__init__(self)
        print("Bad line in file. ", message)


class FileEmpty(StudentsDataException):
    # Write your code here.
    def __init__(self):
        StudentsDataException.__init__(self)
        print("File empty")


def user_input():
    # This function prompts user to input name of file
    while True:
        try:
            #ui = input("Input name of file to process: ")
            #s = open(ui, "rt")
            s = open("Jekyll.txt", "rt")
            return s
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno)) 


def evaluate_file(stream):
    try:
##        if len(stream) == 0:
##                raise FileEmpty()
    
        for line in stream:
            if len(line) == 1:
                raise BadLine("Line is empty")
                #raise BadLine()
            print(line, end = "")
    except BadLine:
        pass



def students_results():
    # 
    # File open is here
    stream = user_input()
    lines = evaluate_file(stream)
      
    

def file_output():
    # Printing to file is here
    try:
        s = open(file+".hist", "wt")
        for entry in characters.items():
            s.write(entry[0] + " -> " + str(entry[1]) + "\n")
        s.close()
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))
    


if __name__ == "__main__":
    students_results()
