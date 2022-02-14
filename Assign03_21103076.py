
##################  ques1  #######################

a=str(input("enter string: "))
list=a.split()           #split a with delim as space and store in list
dict={}                  #create empty dictionary

if list.__len__()==1:    #if length of list is 1 i.e (only one word enter by user)
    for i in list[0]:
        if i in dict:    # update key value pair if same character is found in dict
            dict[i] +=1
        else:
            dict[i]=1
    print(dict)   
else:                    #if more than one word enter by user
    for i in list:
        if i in dict:    #update key value pair if same word is found in dict
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")

###################  ques 2  ######################

def next_date(day,month,year):
    cond=1                                    #cond represent condition and initializing condition to 1
    new_year=year
    if 1800<=year<=2025:                       #leap year or not doesnot matter 
        if month in [1,3,5,7,8,10,12]:                  #case of 31 days in month
            if month!=12:                                      # not include december here
                if 1<=day<=31:
                    if day==31:                                     #last date of month
                        new_day=1                        
                        new_month=month+1
                    else:
                        new_day=day+1                                # in same month
                        new_month=month
                        
                else:
                    print("you entered wrong day")    
                    cond=0                             # change condition value to 0 so that while loop can run again
                    return 
            else:                                               # if month is december
                if 1<=day<=31:
                    if day==31:                                       # case of last day of year
                        new_day=1
                        new_month=1
                        new_year=year+1
                    else:
                        new_day=day+1
                        new_month=month           
        elif month in [2,4,6,9,11]:                     #case of 30 days in month
            if month!=2:                                       #not included february month here   
                if 1<=day<=30:
                    if day==30:                                      #last date of month
                        new_day=1
                        new_month=month+1
                        
                    else:
                        new_day=day+1                                # in same month
                        new_month=month
                else:
                    print("you entered wrong day")
                    cond=0                           # change condition value to 0 so that while loop can run again
                    return
            elif year%4!=0:                
                if day==28:                                 # case of february month and non leap year  
                    new_day=1
                    new_month=month+1
                else:
                    new_day=day+1              
                    new_month=month
            else: 
                if day==29:                                  # case of february month and leap year
                    new_day=1            
                    new_month=month+1
                else:
                    new_day=day+1                                   # in same month
                    new_month=month
        else:
            print("you entered wrong month")      
            cond=0
            return
    else:
        print("you entered year not in range")
        cond=0                                      # change condition value to 0 so that while loop can run again
        return
    if cond==1:
        print("Next Date is : ",new_day,"/",new_month,"/",new_year)
        global cond1
        cond1=1                                     #change condition and break while loop if details enter is coorect
        return


cond=0                                    # condition value is 0so that while loop can run again if user enter wrong details
while cond==0:
    day=int(input("enter day: "))
    month=int(input("enter month: "))
    year=int(input("enter year: "))
    next_date(day,month,year)
    if cond1==1:
        break


################  ques 3  ######################

print("enter elements of list seperated by ',' ")
# taking input elements and converting string element to integer taking delimiter as ',' and store as list 
input_list=[int(x) for x in input().split(',')] 
#creating empty list
square_list=[]
#append elements in square_list
for i in range(len(input_list)):
    square_list.append((input_list[i],input_list[i]*input_list[i]))
print(square_list)    


################  ques 4  #######################
def grade_point(point):   
    # check if the grade point meets the range
    if point>10 or point<4:
        print("Invalid grade point! Try Again")
        return
    #using switcher function to directly switch to point that student get                          
    switcher= {
                4: "Your Grade is 'D' and poor performance",
                5: "Your Grade is 'C' and Below Average performance",
                6: "Your Grade is 'C+' and Average performance",
                7: "Your Grade is 'B' and Good performance",
                8: "Your Grade is 'B+' and Very Good performance",
                9: "Your Grade is 'A' and Excellent performance",
                10:"Your Grade is 'A+' and outstanding performance",
    }
    # change condition to break while loop    
    global cond1
    cond1=1
    return switcher.get(point, "nothing")
   
cond=0            #represent condition ,initializing condition so that while loop works
cond1=0         
while cond==0:      
    point=int(input("enter grade points : "))     
    print(grade_point(point))     
#As details of student grade print condition 1 changes to 1 and while loop break
    if cond1==1:     
        break

###################  ques 5  ###################

k=6
for i in range(k):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(k-i)-1):
        print(chr(65 + j), end='')  #ASCII VALUE OF A=65,B=66,C=67,.......,J=74,K=75
    print()
print("\n")    
 

###################  ques 6  ###################

Sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {Sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        Sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[Sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("<a>",students)

#part b. sort acc to the names
print("<b>",{p:q for p,q in sorted(students.items(), key=lambda x:x[1])})

#part c. sort acc to the SIDs
print("<c>",{p:q for p,q in sorted(students.items())})

#part d. search for a student by their SID
Sid = int(input("Search Name with SID: "))
print("<d>",students[Sid])


####################  ques 7  #####################

def recur_fibo(n):        #using recursion toget fibonacci termas and its avg 
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES: "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0                          #initialize sum as 0
   for i in range(no_of_terms):
       print(recur_fibo(i))       
       sum=sum+recur_fibo(i)        #add fibonacci terms to sum 
avg=float(sum/no_of_terms)
print("AVERAGE OF RESULTANT FIBONACCI SERIES IS",avg)


#####################   ques 8    #######################

#given sets 
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)









