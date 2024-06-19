#Write a program that reads data from a CSV file and prints it to the console.
import csv
with open('data.csv','r') as file :
    csv_reader = csv.reader (file)
    for row in csv_reader:
        print (row)