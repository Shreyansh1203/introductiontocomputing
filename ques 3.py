#question 3:make a list of SID,NAME,GENDER,COURSE NAME,CGPA
#answer: source code
#taking input information from user
Name=input("Please enter name: ")
SID= input("Enter student Id: ")
Gender=input("Enter gender: ")
Gender=str(Gender)
if (Gender=='male'or Gender=='m'):
    Gender='M'
if (Gender=='female'or Gender=='f' ):
    Gender ='F'
if (Gender=='unknown'):
    Gender='U'
CGPA=input("Enter CGPA: ")
Course_name=input("Enter course name: ")
SID=int(SID)
CGPA=float(CGPA)
#our list now name as student_info
data=['Name','SID','Gender','Course name','CGPA']
print(data)
student_info=[Name,SID,Gender,Course_name,CGPA]
print(student_info)
