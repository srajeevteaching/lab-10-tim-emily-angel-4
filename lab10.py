# Programmers: Tim Hunt, Emily Catanzariti, Angel Scott
# Course: CS151, Dr. Rajeev
# Date: 12/2/2021
# Lab Number: 10
# Program Inputs: Name of file containing Morse Code
# Program Outputs: Decoded file contents

ENGLISH = 0
MORSE = 1

def load_morse_dictionary():
    try:
        morse_code_file = open("morsecode.txt", "r")
        morse_codes = []
        for line in morse_code_file:
            code = line.strip().split("\t")
            morse_codes.append(code)
        morse_code_file.close()
        morse_code_dictionary = {}
        for i in morse_codes:
            morse_code_dictionary[i[MORSE]] = i[ENGLISH]
    except FileNotFoundError:
        print("Error. File not found.")
    return morse_code_dictionary

def decode_file(file_name, dictionary):
    try:
        new_file = open(file_name, "r")
        new_file_morse = []
        for line in new_file:
            line = line.strip().split()
            new_file_morse.append(line)
        new_file.close()
        for i in new_file_morse:
            if i in dictionary:
                print(dictionary[i])
    except FileNotFoundError:
        print("Error. File not found.")
