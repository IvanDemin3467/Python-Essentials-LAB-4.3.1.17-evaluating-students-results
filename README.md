# Python-Essentials-LAB-4.3.1.17-evaluating-students-results

**Objectives**

•	improve the student's skills in operating with files (reading)

•	perfecting the student's abilities in defining and using self-defined exceptions and dictionaries.

**Scenario**

Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:
```
John	Smith	5
Anna	Boleyn	4.5
John	Smith	2
Anna	Boleyn	11
Andrew	Cox	1.5
```
Your task is to write a program which:

•	asks the user for Prof. Jekyll's file name;

•	reads the file contents and counts the sum of the received points for each student;

•	prints a simple (but sorted) report, just like this one:
```
Andrew Cox 	 1.5
Anna Boleyn 	 15.5
John Smith 	 7.0
```
Note:

•	your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;

•	implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file exists but is empty.

Tip: Use a dictionary to store the students' data.

**Job is done. Complet code includes**
```
class StudentsDataException(Exception):

class BadLine(StudentsDataException):
    # This exception is raised in many cases if file contains bad lines

class FileEmpty(StudentsDataException):
    # This exception is raised in a case of empty file

def user_input():
    # This function prompts user to input the name of the file

def evaluate_file(stream):
    # This function evaluates the data in the file and converts it into list

def students_results():
    # This function processes results stored in a list;
    # perfoms grades summation;
    # converts results into a dict;
    # and prints report to cmd
```
