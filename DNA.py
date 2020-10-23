# Implement a program that identifies a person based on their DNA, per the below.
from cs50 import get_float, get_int, get_string
# Documentation for argparse can be found at: https://docs.python.org/3.3/library/argparse.html
# Python's sys module gives you access to sys.argv for command-line arguments
import sys
from sys import argv, exit
# Python's csv module has reader and DictReader
import csv
from csv import reader
# Regex was recommended by discord CS50. https://docs.python.org/3/library/re.html && https://pypi.org/project/regex/
import re

# Beginning code could be found in Lecture 6

def main():
    i = compute()
    ## j = comparison_str(STR_string, csv_files) // Turns out, I didn't need to call this

# We will need to do the compute first since it is step 2
def compute():
    # The program should require as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.
    if len(argv) != 3:
    # To open the file https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
        print("Please input in the correct command lines for the csv file and text file.\n")
        exit(1)

    # If they enter in the correct command, it should open the file
    # Documentation can be found here: https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    databases_csv = argv[2]
    with open(databases_csv) as csv_file:
        if csv_file.mode != "r":
        # If the file is not a readable file, it should close let the user know. And it should be closed
            print(f"{argv[2]} can not be read.\n")
            exit(1)
        # If it works, it should open
        csv_files = csv.reader(csv_file)
        # print(csv_files)
        for row in csv_files:
            print(row)
            # str_list = row
            #print(str_list) // It prints out the letter and not the actual string
    
    # We will store the str_list into a list
    #RNA = str_list[0]
    # print(RNA)
    
    # We should create a str_sequence dictionary so that it would be populate
    str_sequence = {}
    # A second empty dictionary so that we can copy over the STR values so we can do a side-by-side comparison
    empty_sequence = {}

    # The second file that should be opened should be the database_csv
    with open(argv[1], "r") as database_csv:
        # If it works, it should open
        database_reader = csv.reader(database_csv)
        # We want to load up the STR to analyze them properly
        next_column = len(next(database_reader))
        database_csv.seek(0)
        header = list(next(database_reader))
        header.pop(0)
        # print(header) #// Testing to make sure it works
        
    # For each of the STRs (from the first line of the CSV file), your program should compute the longest run of consecutive repeats of the STR in the DNA sequence to identify.
    # We started with header[1:] because the first column is name
        for STR_string in header[1:]:
        # By doing this, we will populate the empty dictionary with the STR and the amount of STR
        # We are copying the list into the dictionary and then we will link and compare the the two    
            empty_sequence[STR_string] = 1
            #print(empty_sequence)
            
            str_sequence[STR_string] = comparison_str(STR_string, csv_files)
            #print(str_sequence)
        
        #for item in header:
            #empty_sequence[item] = 1
            #print(empty_sequence)
            
    # If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual.
    with open(argv[1], newline = ' ') as file:
        csv_dict = csv.DictReader(file)
        for row in csv_dict:
            STR = 0
            for STR_string in str_sequence:
                # int(x) takes the string x and turns it into the integer
                if str_sequence[STR_string[1:]] == int(row[STR_string]):
                # Testing to see how what would work
                ##print(row[STR_string])
                ##print(int(STR_string))
                ##print(int(STR_string))
                    STR += 1
                    #print(str_sequence[STR_string[1:]])
                    #print(STR)
                    #print(int(row[STR_string]))
            # s[i:j] in Python takes the string s, and returns the substring wth all characters from the ith character up to , but not including the jth
            #if STR == len(str_sequence):
                #print(row['name'])
                #exit()
        #else:
            #print("No match.\n")


def comparison_str(STR_string, csv_files):
    # Received help from : https://stackoverflow.com/questions/61206239/how-to-count-longest-sequence-of-recurring-characters-in-very-long-string-inside
    # Also received help from https://stackoverflow.com/questions/62513515/cs50-pset6-dna-no-match-using-regex-to-count-st
    # Received help w the code: https://stackoverflow.com/questions/62916456/how-to-find-the-max-number-of-times-a-sequence-of-characters-repeats-consecutiv
    # regex compile. We decided to do a re.compile because it uses both match and search
    # First we need to create a counter to match large.csv and small.csv so we know which names match and which doesn't
    counter = 0
    max_counter = 0

    # To find out the sequence and pattern, we will use regex - both for search and athe match
    repeating = re.findall(rf"(?:{STR_string}){{2,}}", csv_files)

    # According to the previous aforementioned stack over-flow, it recommends that we do a result(begin) - results(end)
    # The code for the findall is: https://stackoverflow.com/questions/62916456/how-to-find-the-max-number-of-times-a-sequence-of-characters-repeats-consecutiv
    for matches in repeating:
        counter = len(matches) / len(repeating)
        if counter > max_counter:
            max_counter = counter
    return int(max_counter)



if __name__ == "__main__":
    main()
