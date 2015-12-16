# Python-lab
Python lab programs
LIST OF ASSIGNMENTS/PROGRAMS
Pgm No
Title of the program/ Problem Statement
1
Write a line of code using lambda function along with map/reduce/filter functions to do the following:-
a) Given x and n (read as user input), create a list having powers of x from 1 to n
Eg: If x=2,n=5 the result must be [2,4,8,16,32]
b) Given a list of strings, remove all strings having first character as digit
c) Given a list of numbers, find maximum in the list
d) Given a list of tuples containing two integers, remove all tuples where second element in tuple is not a factor of first element.
e) Given a list of integers, combine all integers to form a single integer.
Eg: [1,25,32,4,5] ==> 1253245
Write a client-server program using sockets. Client sends a tuple containing two strings. One is the input string and other is a string which denotes operation to be performed on the input string. Once the server receives the tuple, it performs the operation on the string and sends the result back to the client where it is printed.
 If the operation is "rev", server must reverse the string.
 If the operation is "cap", server must convert the string to uppercase.
 If the operation is "encr", server must encrypt the string. [ "abc" -> "bcd", "time" ->"ujnf" ]
 If the operation is not defined, server must send back "Invalid Operation".
Demonstrate TCP and UDP communication.
2
Given a file “stateinfo.txt” containing names of the state and cities separated by “:”, create a file for each state named as “statename”.txt containing names of cities in that state. Sample input file “stateinfo.txt” is attached. Steps to follow:
Walk through the file. Create a dictionary whose key is the state name and value is the file handle. Write city names into the file.
Do close all the files at the end of processing using values in dictionary.
Create table employee with fields ID primary key, name, age, salary, deptid(foreign key refers id in dept)
a) Find youngest employee from each department
b) Display department name and total number of employees in that department
c) Find the department name with the highest paid employee. Also display employee name
3
Create a dictionary for words and their meanings. Write functions to add a new entry (word:meaning) , search for a particular word and retrieve meaning, given meaning find words with same meaning , remove an entry, display all words sorted alphabetically. [Program must be menu driven]
Given an input file which contains list of names, phone numbers and email-ids separated by spaces in the following format:-
Alex 80-23425525 alex234@yahoo.com
Emily 322-56775342 em_44@gmail.com
Grace 20-24564555 softech_grace@rediffmail.com
Phone number contains 3 or 2 digit area code and a hyphen followed by 8 digit number
Perform the following using regular expressions:-
a) Find all phone numbers having 4 consecutive 0s at the end.
b) Find all names having phone numbers with 3 digit area code.
c) Find the total number of people having gmail id.
d) Find user name part of email id for all people whose name start with 'G' or 'E' and ends with 'y'
e) Find all names whose phone numbers are not in proper format.
4
Create a class to represent city which contains a list of places to see.
- Provide methods to create the object with just the city name or with city name and places (stored as list)
- Provide methods to add a place of visit, to remove place of visit, to display all places of visit.
Add exceptional handling so that remove does not crash if the given place is not in the city
Given an input file, do the following using regular expression and create an output file.
a) Remove extra whitespaces between two words.
b) Insert a white space after the end of a sentence (after . or ? or !).
c) First letter of each sentence should be upper case
d) Remove consecutive duplicate words.
5
Create a package Shapes which contains modules Circle, Square, Triangle and Util.
 Circle module has functions to compute area and circumference of a circle given radius.
 Square module has functions to compute area and perimeter of a square given side.
 Triangle module has functions to compute area and perimeter of a scalene triangle given three sides.
 Util module has functions to compute square of a number, square root of a number and a variable pi with value 3.14.
 Circle, Square and Triangle modules must use data and functions in Util module to compute area, circumference etc.
Write client program (menu driven) which reads required input information for circle, square or triangle and make use of package Shapes to call respective functions.
Experiment with ply
Tokenize the following as follows:
abc * b => (abc, ID) (*, OP) (b, ID)
pq ** b => (pq, ID) (**, OP) (b, ID)
ab < bc + cd => (ab, ID) (< , OP) (bc, ID) (+, OP) (cd, ID)
p --- q => (p, ID) (--, OP) (-, OP) (q, ID)
6
i. Write python code to remove all empty files in a given path.
ii. Given a path, traverse the path and display all files and subdirectories in each level till the deepest level. Also display total number of files and subdirectories.
Experiment using regular expressions -
The file test.py has the following code:
import re
print(help(re))
Run the program test.py as follows.
python3 test.py > re.doc
Process this file re.doc. Find all functions (print only function names) declared between FUNCTIONS and DATA sections.
7
Given n, generate Pascal triangle for n rows. Use list of lists.
If n = 5, output should be
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Write a program to sum the elements of an array (list) using 4 threads. Let each thread add quarter of the array. Assume that the size of the array is a multiple of 4. Use global variable “total_sum” which gets updated by each thread once it computes partial sum. Use lock when global variable is getting updated.
8
Create a module named Area which has functions to compute area of circle, rectangle and scalene triangle. Function to compute area of circle takes radius as argument, function to compute area of rectangle takes length and breadth as arguments and function to compute area of triangle takes lengths of three sides as arguments.
- Write client code (menu driven) which imports module Area, reads the input from user and invoke appropriate functions.
- When module Area.py is executed as a python script, you must be able to specify command line arguments of the form as shown below:-
 python Area.py circle 4 # this should invoke the function to compute area of circle with radius 4
 python Area.py rect 4 5 # this should invoke the function to compute area of rectangle with length 4 and breadth 5
 python Area.py tri 3 4 5 # this should invoke the function to compute area of triangle with sides 3, 4 and 5
- If the required number of arguments for a shape is not specified or if the number of arguments is more than what is required, give appropriate error message and exit.
Demonstrate the following:-
a) Try importing different ways
b) Save the module in different path and try importing.
Do the following using regular expressions:-
a) Find all occurrences of a word in a multiline string. The search must be case insensitive. Also find and display the starting index of each matched word in the input string.
b) Given a line of text find all characters other than vowels and space characters.
c) Given a list of strings find all strings that start with a digit or an underscore.
Write a function which gets no: of strings using variable no: of arguments and find unique characters in each string.
Write a function which concatenates all given strings to a single string.
User can specify sep - default should be comma.
User can specify first string - default should be 'result: '
Write a program where one process acts like a server and the other the client. Each time the client communicates a number, the server returns the square of it. Avoid racing using semaphores. Avoid catering to the same request twice. Let parent process (client) read the number from keyboard and child process (server) computes the square and prints it and this must happen continuously until the number sent is -1. If the number sent is -1, terminate the child process and end the program. Make use of shared variable.
10
Write an iterator (class) that returns numbers in the Fibonacci series for a given range.
If the range is 30, it should return 0 1 1 2 3 5 8 13 21
Create a table which has name and date of birth of a person.
(Use date type for date of birth, enter date as ‘yyyy-mm-dd’)
a) Read the name and date of birth from the keyboard for four records, store them in a list of tuples and insert into the table. (Use executemany function)
b) Display the name and the age of the person (in years).
Check julianday() function
julianday(d1)-julianday(d2) gives the difference between two dates in no of days
c) Find all persons whose birthday falls in a given month (eg: input is ‘04’ for april,’01’ for jan)
11
Create a class called MyStack which supports push, pop and display operations.
 Implement the stack class using a list. Specify the upper bound of the size while creating the stack object.
Provide exception handling mechanism for stack overflow and stack underflow.(Use user-defined exception classes)
Write a graphic based program using Tkinter. Provide two entry boxes for user input, radio button group having buttons labelled as add, sub, mul and div and another entry box labelled Result. When inputs are given and one button among the radio button group is selected, corresponding result must be displayed in entry box labelled result.
12
Write a function which prints a message given as argument. Decorate the function twice with different decorators
Assume the function is print_message and the message to be printed is "hello".
Decorating print_message with a function called stars should print :
*****
hello
*****
Decorating print_message twice using dollars and stars should print :
$$$$$
*****
hello
*****
$$$$$
Create a table Person, with fields Name (contains first name followed by last name), Age, AreaofInterest (Music, Dance, Sports, Travel), Occupation
a) Find all persons whose last name is “Sharma”
b) Find the most common area of interest among all persons
c) Delete all entries having area of interest other than ( Music, Dance, Sports, Travel)
Demonstrate autocommit feature in sqlite
13
i. Write a line of code using generator expression for the following:-
(Do not use list comprehension anywhere)
a) Find the longest and second longest word in a multiline string (can use inbuilt sorted method for sorting)
b) Find all words in a line of text where a character repeats anywhere in that word
ii. Write a line of code for the following using list comprehension.
a) Given a list L containing numbers, return a new list with cumulative sum, that is, a new list where the ith element is the sum of first i+1 elements from the original list.
For example, given a list [1,2,3,4] the result should be [1,3,6,10]
b) Find all numbers between a pair of numbers which are perfect squares and sum of all digits in the number is less than 10
Implement two-way communication between parent and child processes using:
a) Pipe
b) Queue
14
i. Write a Generator function which gives the next prime number each time. Use this to find all prime numbers in a given range.
ii. Write a program to validate a given date. Input date in the format dd/mm/yyyy. Check also for leap year.
Write a graphics based program using Tkinter. Main window must have dimensions 250 x 200 placed at 100,100 from top left. Provide one button with background color “red” labelled “Click Me”, one label having initial text “Not Clicked Yet” with background color “blue” and a button labelled “EXIT”. On first click of the button, the label text must change to “1 click” and font must change to Times, Bold and size 20. On every subsequent click, label text should show how many clicks. On even click, background color of label must change to “purple” and on odd click, it must change to “green”. When button labelled “EXIT” is clicked, it should exit the GUI.
