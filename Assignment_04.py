

#############  ques 1  #############

def tower_of_hanoi(n,a,b,c):                            # a is source , b is helper , c is destination
    if n==1:
        print("move 1st disk from",a, "to" ,c)
        return
    tower_of_hanoi(n-1,a,c,b)                           # recursive call foer n-1 disk in which c act as helper  
    print ("move", n,"th disk from ",a,"to", c)
    tower_of_hanoi(n-1,b,a,c)                           # recursive call foer n-1 disk in which a act as helper  
tower_of_hanoi(3,"source","helper","destination")     

################   ques2  #####################
from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))

print("by loop")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")                #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	      # nCr = n!/((n-r)!*r!)
	print()	                          #  for new line
print("\n\n")

print("using recursion")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i                # using Binomial Coefficient                         

    print()
pascal_triangle(n)
print("\n")



#############  ques 3  ##############
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#part <a>
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part <b>
if (Quotient == 0):
    print("<b> The quotient is zero")
if (Remainder == 0):
    print("<b> The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("<b> All the values are non zero")

#part <c>
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"<c> Filtered out numbers that are greater than 4 are : {result}")

#part <d>
setresult = set(result)
print("<d> Set:",setresult)

#part <e>
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("<e> Immutable set:",immutableSet)

#part <f>
print("<f> Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")

#############   ques 4  ################
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")

student1 = Student("shreyansh", 21103076) #creating object
print("Object created")
print(f"The name of the student it {student1.name} and SID is {student1.roll_no}.")  #print the assigned values
del student1  #deleting object
print("\n")


############  ques 5 ###############

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part <a> updating salary
employee1.salary = 70000
print(f"<a> The updated salary of {employee1.name} is {employee1.salary} ")
#part <b> deleting a record
print("<b>Record of Viren deleted", end='')
del employee3
print("\n")

###########  ques 6 ##############
#inputting a word from the first friend
word =input("Enter the word: ")
word=word.lower()

#input a meaningful word with the exact same letters
testword = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
testword=testword.lower()
#define dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()






