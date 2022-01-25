
#Ques1: Run the following commands on the string


#Define the string
sentence = "Python is a case sensitive language"

#Part a: print length of sentence
print("Part a: Length of the string = ", len(sentence))

#Part b: Reverse the order of string in one line code
print("Part b: Here's the reverse order =\n",sentence[::-1])

#Part c: using slice function store "a case sensitive" in another string
new_string = slice(10,26)
print("new variable = ", sentence[new_string])

#Part d: Replace "a case sensitive" with "a object oriented"
print("Part d:asked replacement = ", sentence.replace("a case sensitive", "a object oriented"))

#Part e: Index of "a"
print("Part e:index of 'a' =", sentence.find("a"))

#Part f: Remove white spaces
print("Part f:string without white spaces:", sentence.replace(" ",""))
                      

#Ques 2: Store your name, SID, department name and CGPA into different variables.
# With the help of String formatting print the following output...

#Asking user for input
name = input("Enter your name:")
SID = input("Enter your SID: ")
department = input("Enter your dept.:")
CGPA = input("Enter your CGPA:")

#Printing the statement with the asked formatting.
print("Hey, %s Here! \nMy SID is %s \nI am from %s department and my CGPA is %s" %(name, SID, department, CGPA))


#Ques 3: For a=56 and b=10 with the help of bitwise operators calculate the following
#Define variable and their value

a = 56
b = 10
print('a=',a)
print('b=',b)
#Part a: a&b
print("Part a: a&b = ", a&b)

#Part b: a|b
print("Part b: a|b = ", a|b)

#Part c: a^b
print("Part c: a^b = ", a^b)

#Part d: Left shift both a and b with 2 bits
print("Part d: Left shift a = ", a << 2)
print("Part d: Left shift b = ", b << 2)

#Part e: Right shift both a with 2 bits and b with 4 bits
print("Part e: Right shift a = ", a >> 2)
print("Part e: Right shift b = ", b >> 4)

#Ques 4: Write a python program to find the greatest of three numbers entered by the user.

#Take inputs of three numbers a,b and c
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

#Using if else to find largest number
if (a>b):
  if (a>c):
   largest = a
  else:
    largest = c
elif (b>c):
  largest = b
else :
 largest = c
print("The largest number is", largest)


#Ques 5: Write a python program to check if the word “name” is present in
#the string entered by the user (Print : “Yes” or “No”).


#Take input from user
statement = str(input("Please type a statement:\n"))

#Condition to find "name"
if "name" in statement:
    print("Yes")
else:
    print("No")


#Ques 6: Program to find if triangle exists or not.


#Take inputs for three sides of a triangle:
side1 = int(input("Enter first side:\n"))
side2 = int(input("Enter second side:\n"))
side3 = int(input("Enter third side:\n"))

#Putting conditions using if else
if side1 + side2 < side3:
    print("No")
elif side2 + side3 < side1:
    print("No")
elif side1 + side3 < side2:
    print("No")
else:
    print("Yes")


