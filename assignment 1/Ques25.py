#Write a program that copies the contents of one text file to another.

def copy_file_contents(original_file, destination_file):
    try:
        
        with open(original_file, 'r') as src:
            
            contents = src.read()
        
        
        with open(destination_file, 'w') as dest:
           
            dest.write(contents)
        
        print(f"Contents copied from {original_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
    except IOError:
        print("Error: An I/O error occurred.")


source_file = 'source.txt'        
destination_file = 'destination.txt'  

copy_file_contents(source_file, destination_file)
