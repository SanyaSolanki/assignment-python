#Write a python program that calculates the factorial of a given number.

def factorial_of_a_num(num):
    count=1
    if num==0 or num==1:
        print("Factorial is 1")
    else:
        count=num*factorial_of_a_num(num-1)
    return count
a=int(input("Enter the number "))
print("The factorial of",a,"is: ",factorial_of_a_num(a))
