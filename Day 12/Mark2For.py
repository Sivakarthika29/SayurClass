######### Problem 1.1
#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67


nameList = []
markList = []
noOfStudents = 3
noOfmarks = 2
for student in range (1, noOfStudents+1):
    name =input("Enter your name : ")
    nameList.append(name)
    for mark in range (1,noOfmarks+1):
        inputMark = float(input(f"Enter your mark {mark} : "))
        markList.append(inputMark)

mark = 0
for student in nameList:
    print(f"{student}'s marks {markList[mark]} , ",end="")
    mark = mark + 1
    print(markList[mark])
    mark = mark + 1