 #Write a python program that returns the minimum and maximum values in a list of numbers.
def min_max(num):
    min_value=num[0]
    max_value=num[0]

    for i in num:
        if i< min_value:
            min_value=i
        if i> max_value:
            max_value=i
    return min_value,max_value
lst=[1,3,4,2,8,-3,5,-7,-32,89,-66,100]
a,b=min_max(lst)
print("The minimum value in the list is ",a)
print("The maximum value in the list is ",b)
