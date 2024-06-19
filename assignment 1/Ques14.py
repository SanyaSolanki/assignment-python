#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines=[]
while True:
    sentence=input("Enter a line")
    if sentence=="":
        break

    lines.append(sentence)

print("Reading the text")
for line in lines:
    print(line)