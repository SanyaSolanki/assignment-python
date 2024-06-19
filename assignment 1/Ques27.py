#Write a program in python that converts a string into a list of its characters.

def string_to_char_list(string):
    char_list = list(string)
    return char_list

input_string = input("Enter a string: ")

character_list = string_to_char_list(input_string)
t
print("List of characters:", character_list)
