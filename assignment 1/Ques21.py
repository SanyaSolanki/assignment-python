#Write a python program that counts the occurrences of a specific element in a list.
def occur(l,ele):
    count=0
    for i in l:
        if i==ele:
            count+=1
    return count
lst=[1,2,4,1,6,7,3,4,6,4,6,9,7,6]
element=4
occurences=occur(lst,element)
print(f"The no. {element} occur {occurences} times in the list")