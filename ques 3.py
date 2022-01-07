#question 3:make a list of SID,NAME,GENDER,COURSE NAME,CGPA
#answer: source code
#taking input information from user
Name=input("Please enter name: ")
SID= input("Enter student Id: ")
Gender=input("Enter gender: ")

Course_name=input("Enter your course name: ")
CGPA=input("Enter CGPA: ")
SID=int(SID)
CGPA=float(CGPA)
#our list now name as student_info
data=['Name','SID','Gender','Course name','CGPA']
print(data)
student_info=[Name,SID,Gender,Course_name,CGPA]
print(student_info)
