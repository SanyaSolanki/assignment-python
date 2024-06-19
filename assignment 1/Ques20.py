#Write a python program that takes a list of numbers and returns their sum.
a=int(input("Enter the length of the string"))
l=[]
sum=0
for i in range(0,a):
    number=int(input("Enter a number"))
    l.append(number)
    sum+=number
print("The sum of the integers in the list",l)
print(sum)