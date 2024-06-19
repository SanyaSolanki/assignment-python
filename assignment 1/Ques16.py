#Write a program in python that counts the frequency of each character in a string.
def count_char(string):
    count={}
    for i in string:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
sentence=input("enter a string ")
print("Character frequencies")
print(count_char(sentence))