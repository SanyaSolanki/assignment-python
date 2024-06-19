#Write a program that reads the content of a text file and prints it to the console.

Sentence = input("Please enter a string: ")
filename = "user_input.txt"

with open(filename, 'w') as file:
    file.write(Sentence)

print(f"Input has been written to {filename}.")

try:
    # Open the file in read mode and read its content
    with open(filename, 'r') as file:
        content = file.read()
    
    # Print the content to the console
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")

