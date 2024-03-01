######## Problem  1 ###############
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

# for student in range (#FillinMissingCode):
#     #FillinMissingCode  to get studnet name
#     for mark in range (#FillinMissingCode):
#         inputMark = float (input(f"#FillinMissingCode")) #use formatted string
#         print (#FillinMissingCode)

markList = []
noOfStudents = 3
noOfmarks = 2
for student in range (1, noOfStudents+1):
    name =input("Enter your name : ")
    for mark in range (1,noOfmarks+1):
        inputMark = float(input(f"Enter your mark {mark} : "))
        markList.append(inputMark)

student = 1
for i in range(0, len(markList),2):               # 0 , 2 , 4 , 6
    print(f"Mark 1 for Student {student} is {markList[i]}")
    print(f"Mark 2 for Student {student} is {markList[i+1]}")
    student =student+1
    if i == len(markList)-2:                      # 6 - 2 = 4   # 4 == 4
        break

# OUTPUT:

# Enter your name : Sivashankar 
# Enter your mark 1 : 98
# Enter your mark 2 : 97
# Enter your name : Sivaranjani
# Enter your mark 1 : 99
# Enter your mark 2 : 95
# Enter your name : Sivakarthika
# Enter your mark 1 : 92
# Enter your mark 2 : 94
# Mark 1 for Student 1 is 98.0
# Mark 2 for Student 1 is 97.0
# Mark 1 for Student 2 is 99.0
# Mark 2 for Student 2 is 95.0
# Mark 1 for Student 3 is 92.0
# Mark 2 for Student 3 is 94.0
