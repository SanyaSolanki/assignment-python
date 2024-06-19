
Sentence = input("Please enter a string: ")
filename = "user_input.txt"

with open(filename, 'w') as file:
    file.write(Sentence)

print(f"Your input has been written to {filename}.")
