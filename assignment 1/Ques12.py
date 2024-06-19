# Write a python program that calculates the sum of the digits of a given number.
def sum_of_digits(number):
    str_num=str(number)
    total=0
    for i in str_num:
        total+=int(i)
    return total
num=int(input("Enter a number "))
sum_digits=sum_of_digits(num)
print(f"The sum of the digits of number {num} is ",sum_digits)