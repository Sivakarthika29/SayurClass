#Write a program that will swap two numbers.
#Using function

def swap(first_num, sec_num):
    print("Before Swapping, first number:", first_num,",second number:", sec_num)
    temp=first_num
    first_num=sec_num
    sec_num=temp
    print("After Swapping, first number:", first_num,",second number:", sec_num)
swap(int(input("Enter the first number:")),int(input("Enter the second number:")))
