#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

def check_prefix_suffix(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    ends_with_suffix = string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix

sentence = input("Enter a string: ")

prefix = input("Enter the prefix to check: ")

suffix = input("Enter the suffix to check: ")

starts_with, ends_with = check_prefix_suffix(sentence, prefix, suffix)
print(f"Does the string start with '{prefix}'? {'Yes' if starts_with else 'No'}")
print(f"Does the string end with '{suffix}'? {'Yes' if ends_with else 'No'}")
