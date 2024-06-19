#Write a python program that removes all punctuation from a given string.

def remove_punc(input_string):
    punc_chars = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    cleaned_string = ""
    
    
    for char in input_string:
        
        if char not in punc_chars:
            
            cleaned_string += char
    
    return cleaned_string

input_string = input("Enter the string")
cleaned_string = remove_punc(input_string)
print("Original string:", input_string)
print("String without punctuation:", cleaned_string)
